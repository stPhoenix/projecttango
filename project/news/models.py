from django.db import models

# Create your models here.
TITLE_MAX_LENGTH = 90


class Article(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    pub_date = models.DateTimeField()
    article_text = models.TextField()
    image = models.ImageField(upload_to='article_images/')