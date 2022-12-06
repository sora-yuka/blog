from django.contrib import admin
from applications.post.models import (
    Post, Category, Comment
)


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)