from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView #Для создания класса 
from Area.models import Place, Info #Для работы с БД 

# Create your views here.
class PlacesView(ListView):
    model = Place
    context_object_name = "place"
    template_name = "places.html"

class InfoView(ListView):
    model = Info
    context_object_name = "info"
    template_name = "info.html"
    