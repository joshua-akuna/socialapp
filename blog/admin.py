from django.contrib import admin

# Register your models here.
from .models import Category, Profile, Post, Comment
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)