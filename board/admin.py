from django.contrib import admin

from .models import Board, Post, Tag

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Tag)
