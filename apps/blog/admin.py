from django.contrib import admin
from apps.blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'view_on_project')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'date_added', 'is_active')


admin.site.register(Post, PostAdmin) 
admin.site.register(Comment, CommentAdmin) 

