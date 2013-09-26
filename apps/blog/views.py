from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.blog.models import Post, Comment


def post_list(request):
	# post_list = Post.objects.all() # This is a simple django query
	post_list = Post.objects.get_all_active() # This is a own query using GenericManager (apps.blog.models)
	return render_to_response("post_list.html", locals(), context_instance=RequestContext(request))


def post(request, id_post):
	post = get_object_or_404(Post, pk=id_post)
	comments = post.get_comments(); #get_comments method is on apps.blog.models into Post model
	return render_to_response("post.html", locals(), context_instance=RequestContext(request))


