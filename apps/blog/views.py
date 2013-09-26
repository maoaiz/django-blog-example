from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from apps.blog.models import Post, Comment


def post_list(request):
	# post_list = Post.objects.all() # This is a simple django query
	post_list = Post.objects.get_all_active() # This is a own query using GenericManager (apps.blog.models)
	return render_to_response("post_list.html", locals(), context_instance=RequestContext(request))


def post(request, id_post):
	post = get_object_or_404(Post, pk=id_post)
	comments = post.get_comments(); #get_comments method is on apps.blog.models into Post model
	return render_to_response("post.html", locals(), context_instance=RequestContext(request))


def new_comment(request, id_post):
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({"error": "You need be logged to comment."}), mimetype="application/json")
    if request.is_ajax():
        if request.method == 'POST':
            post = Post.objects.get_or_none(pk=id_post)  # get_or_none method is on apps.blog.models into GenericManager class
            if post:
                c = Comment(post=post, user=request.user, comment=request.POST.get("comment"))
                c.save()
                response = {"sent": True}
            else:
                response = {"error": "Error, refresh the page"}
        else:
            response = {"error": "Error, the http method is not POST"}
    else:
    	response = {"error": "You are not allowed to be here"}
    return HttpResponse(json.dumps(response), mimetype="application/json")


