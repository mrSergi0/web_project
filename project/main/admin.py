from django.contrib import admin
# Дает возможность зарегать наши модели в админке.
# Register your models here.
from .models import Author, Post, Request

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Request)