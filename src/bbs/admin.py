from django.contrib import admin
from .models import Article, Racer, Book

# Register your models here.
admin.site.register(Article)
admin.site.register(Racer)
admin.site.register(Book)