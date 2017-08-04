from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Article
from django.db import Error

# Create your views here.


class Index(generic.ListView):

    model = Article
    allow_empty = True
    template_name = "news/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context TODO: for complex view


class Detail(generic.DetailView):

    model = Article
    template_name = "news/detail.html"
    context_object_name = "article"

    # def get_context_data(self, **kwargs):
    #     context = super(Detail, self).get_context_data(**kwargs)
    #     #context['article'] = context['article'].comment_set.order_by('-pub_date')
    #     return context


def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.POST['author'] == '' or request.POST['comment_text'] == '':
        return render(request, 'news/detail.html', {
            'article': article,
            'error_message': "You didn't enter author\\text.",
        })
    else:
        try:
            article.comment_set.create(author=request.POST['author'], comment_text=request.POST['comment_text'],
                                       pub_date=timezone.now())
            article.save()
            return HttpResponseRedirect(reverse('news:detail', args=(article_id,)))
        except Error:
            return render(request, 'news/detail.html', {
                'article': article,
                'error_message': "Can't add comment.",
            })
