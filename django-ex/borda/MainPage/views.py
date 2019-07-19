from django.shortcuts import render #Для рендера тимплейтов
from django.template.response import TemplateResponse  #Взаимодействие с Тимплейтами
from django.http import HttpResponse  #Взаимодействие с HTML представлением напрямую
from django.views.generic import ListView #Для создания класса 
from MainPage.models import Categories #Для работы с БД 

class CategoriesView(ListView):  #Потом вызываем в сылках как просмотр
    model = Categories
    context_object_name = 'category'
    template_name = "posts.html"




# Create your views here.
