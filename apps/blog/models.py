from django.db import models
from django.contrib.auth.models import User


class GenericManager(models.Manager):

    def get_all_active(self):
        return self.filter(is_active=True)

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Post(models.Model):
    """Post Model."""
    title = models.CharField(max_length=150, verbose_name="title")
    content = models.TextField(blank=False, verbose_name="content")
    user = models.ForeignKey(User, related_name="user_creator")

    users_likes = models.ManyToManyField(User, null=True, blank=True) #Users list that like this Post. This only is an example to use ManyToManyField!
    
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = GenericManager()

    def __unicode__(self):
        return self.title

    def user_likes_list(self):
        return ", ".join([u.username for u in self.users_likes.all()])

    def get_comments(self):
    	return Comment.objects.filter(post=self.pk, is_active=True)

    class Meta:
        ordering = ('-date_added',)


class Comment(models.Model):
    """Comment Model."""
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    comment = models.TextField(blank=False, verbose_name="comment")
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = GenericManager()

    def __unicode__(self):
        return self.comment

    class Meta:
        ordering = ('date_added',)
