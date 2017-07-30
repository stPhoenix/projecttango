from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article

# Create your views here.


class Index(generic.ListView):

    model = Article
    allow_empty = True
    template_name = "news/index.html"
    context_object_name = "articles"

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context TODO: for complex view


class Detail(generic.DetailView):

    model = Article
    template_name = "news/detail.html"
    context_object_name = "article"