from django.conf.urls import include, url  #Делаем инклюды
from django.views.generic import ListView, DetailView   #Для работы с БД
from . import views  #Подключаем модуль views
'''
После того как ссылка совпадает с со ссылкой в главном приложении,
она обрезается и сравнивается уже здесь. Отсюда мы вызываем методы 
Представления
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'borda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.PlacesView.as_view()),
    url(r'^(?P<pk>\d+)$',views.InfoView.as_view())
    #url(r'^(?P<pk>\d+)$',views.ThreadsView.as_view())
]