from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.blog.models import Post


def post_list(request):
	post_list = Post.objects.all()
	return render_to_response("post_list.html", locals(), context_instance=RequestContext(request))


