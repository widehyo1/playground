from django.contrib import admin
from blog.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass
