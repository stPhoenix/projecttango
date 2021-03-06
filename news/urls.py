"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    url(r'^(?P<page>[0-9]+)/$', views.Index.as_view(), name='index'),
    url(r'^filter/(?P<option>.+)/(?P<variable>.+)/$', views.CategoryTagView.as_view(), name='filter'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.Detail.as_view(), name='detail'),
    url(r'(?P<article_id>[0-9]+)/add_comment', views.add_comment, name='add_comment'),
]