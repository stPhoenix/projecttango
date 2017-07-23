from django.db import models
from news.models import Article
# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment_text = models.TextField(max_length=300)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pub_date = models.TimeField()