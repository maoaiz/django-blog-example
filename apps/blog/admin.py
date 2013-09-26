from django.contrib import admin
from apps.blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'id_user', 'date_added', 'is_active')


admin.site.register(Post, PostAdmin) 
admin.site.register(Comment, CommentAdmin) 

