"""project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from news import views  # Django freaks because no top level import like from ../news import views
from project.settings import TEMPLATE_PREFIX as TP

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='account/'+TP+'/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='news/'+TP+'/index.html'), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'about/$', views.about, name='about'),
    url(r'contact_us/', views.contact_us, name='contact_us'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
