from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Article
from django.db import Error
from django.contrib.auth.decorators import login_required
from project.settings import TEMPLATE_PREFIX as TP

# Create your views here.


class Index(generic.ListView):

    model = Article
    allow_empty = True
    template_name = "news/"+TP+"/index.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context TODO: for complex view


class Detail(generic.DetailView):

    model = Article
    template_name = "news/"+TP+"/detail.html"
    context_object_name = "article"

    # def get_context_data(self, **kwargs):
    #     context = super(Detail, self).get_context_data(**kwargs)
    #     #context['article'] = context['article'].comment_set.order_by('-pub_date')
    #     return context


@login_required
def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.POST['comment_text'] == '':
        return render(request, 'news/'+TP+'/detail.html', {
            'article': article,
            'error_message': "You didn't enter text.",
        })
    else:
        try:
            article.comment_set.create(author=request.user.username, comment_text=request.POST['comment_text'],
                                       pub_date=timezone.now())
            article.save()
            return HttpResponseRedirect(reverse('news:detail', args=(article_id,)))
        except Error:
            return render(request, 'news/'+TP+'/detail.html', {
                'article': article,
                'error_message': "Can't add comment.",
            })

