from django.contrib import admin
from apps.account.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'phone', 'is_active')


admin.site.register(UserProfile, UserProfileAdmin) 

