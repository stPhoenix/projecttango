from django.db import models
from django.utils import timezone
from news.models import Article # Django freaks because no top level import like from ../news import
# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment_text = models.TextField(max_length=300)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '\n Author: %s \n Publication Date: %s \n Comment: %s ' % (self.author, self.pub_date, self.comment_text)
