from django.contrib import admin
from news.models import Article, Category, Tags
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tags)
