from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header = 'User Profile API'


class CustomUserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'full_name', 'date_of_birth')


admin.site.register(UserProfile, CustomUserProfileAdmin)
admin.site.unregister(Group)
