from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.menulist),
    path('B', include('B.urls')),
    path('C', include('C.urls')),
    path('D', include('D.urls')),
]
