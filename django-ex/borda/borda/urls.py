from django.conf.urls import include, url  #Включаем инклюды
from django.contrib import admin  #Включаем админку

urlpatterns = [
    # Examples:
    # url(r'^$', 'borda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  #Попадаем на админку джанго
    url(r'^', include("MainPage.urls")),  #Попадаем на главную страничку
    url(r'^main/', include("MainPage.urls")),
]
