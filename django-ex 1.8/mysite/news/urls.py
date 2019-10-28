from django.conf.urls import include, url#
from django.contrib import admin
from django.views.generic import ListView, DetailView #Для работы с БД
from news.models import Articles
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],template_name = "posts.html")),# Берёт список в обжект лист
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles,template_name = "post.html"))
]
