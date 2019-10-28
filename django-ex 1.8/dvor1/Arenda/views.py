from django.shortcuts import render #Для рендера тимплейтов
from django.template.response import TemplateResponse  #Взаимодействие с Тимплейтами
from django.http import HttpResponse  #Взаимодействие с HTML представлением напрямую
from django.views.generic import ListView #Для создания класса 
from Arenda.models import Place, Info #Для работы с БД 

class PlacesView(ListView):
    model = Place
    context_object_name = "place"
    template_name = "places.html"

class InfoView(ListView):
    model = Info
    context_object_name = "info"
    template_name = "info.html"
