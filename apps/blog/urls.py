from django.conf.urls import patterns, url


blog_patterns = patterns('apps.blog.views',
    url(r'^$', 'post_list', name="post_list"),
    url(r'^post/(?P<id_post>[0-9]+)/$', 'post', name="post"),
    url(r'^post/(?P<id_post>[0-9]+)/new-comment$', 'new_comment', name="new_comment"),
)