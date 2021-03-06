from django.db import models
# Create your models here.
TITLE_MAX_LENGTH = 90
TAG_MAX_LENGTH = 30


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    pub_date = models.DateTimeField()
    article_text = models.TextField()
    image_url = models.URLField(default='media/article_images/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "\n Title: %s \n Publication date: %s \n Category: %s" % \
                (self.title, self.pub_date, self.category.name)


class Tags(models.Model):
    tag = models.CharField(max_length=TAG_MAX_LENGTH)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return "TAG: %s ARTICLE: %s" % (self.tag, self.article.title)


