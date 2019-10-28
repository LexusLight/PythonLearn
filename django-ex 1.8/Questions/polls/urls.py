from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Questions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<question_id>)$', views.detai;, name = "detail"),
    url(r'^(?P<question_id>)$', views.index, name = "index"),
    url(r'^$', views.index, name = "index"),
]