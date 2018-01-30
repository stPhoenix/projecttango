from django.contrib import admin
from news.models import Article, Category, Tags
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'article_title')

    def article_title(self, obj):
        return obj.article.title


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tags, TagAdmin)
