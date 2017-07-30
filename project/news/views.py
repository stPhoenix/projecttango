from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.


def index(request):
    news = Article.objects.all()
    response = ["Tile: %s <br> Publication date %s <br>" % (n.title, n.pub_date)for n in news]
    return HttpResponse("NEWS <br>".join(response))
