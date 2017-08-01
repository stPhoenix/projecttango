from django.db import models

# Create your models here.
TITLE_MAX_LENGTH = 90


class Article(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    pub_date = models.DateTimeField()
    article_text = models.TextField()
    image = models.ImageField(upload_to='article_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "\n Title: %s \n Publication date: %s \n Text: %s \n Image: %s" % (self.title, self.pub_date,
                                                                                  self.article_text, self.image.url)


class Tags(models.Model):
    tag = models.CharField(max_length=60)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=60)
