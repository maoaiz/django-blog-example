from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post Model."""
    title = models.CharField(max_length=150, verbose_name="title")
    content = models.TextField(blank=False, verbose_name="content")
    id_user = models.ForeignKey(User, related_name="user_creator")

    users_likes = models.ManyToManyField(User, null=True, blank=True) #Users list that like this Post. This only is an example to use ManyToManyField!
    
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # objects = PostManager()

    def __unicode__(self):
        return self.title

    def user_likes_list(self):
        return ", ".join([u.username for u in self.users_likes.all()])

    class Meta:
        ordering = ('title',)


class CommentManager(models.Manager):

    def get_all_active(self):
        return self.filter(is_active=True)


class Comment(models.Model):
    """Comment Model."""
    id_user = models.ForeignKey(User)
    id_post = models.ForeignKey(Post)

    comment = models.TextField(blank=False, verbose_name="comment")
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __unicode__(self):
        return self.comment

    class Meta:
        ordering = ('date_added',)
