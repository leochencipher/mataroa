from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main import models


class Admin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "last_login",
        "blog_title",
    )


admin.site.register(models.User, Admin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")


admin.site.register(models.Post, PostAdmin)
