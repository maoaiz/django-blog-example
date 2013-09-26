from django.db import models
from django.contrib.auth.models import User


class UserProfileManager(models.Manager):

    def get_all_active(self):
        return self.filter(is_active=True)


class UserProfile(models.Model):
    """Django User Model extended"""
    phone = models.CharField(max_length=150, verbose_name="phone")
    cell_phone = models.CharField(max_length=150, verbose_name="cell_phone")
    city = models.CharField(max_length=150, verbose_name="city")
    address = models.CharField(max_length=150, verbose_name="address")
    date_born = models.DateField(null=True)

    id_user = models.OneToOneField(User)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = UserProfileManager()

    def __unicode__(self):
        return "%s: %s" % (self.id_user, self.is_active)
