from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView,DetailView #Для создания класса 
from Area.models import Place, Info #Для работы с БД 

# Create your views here.
class PlacesView(ListView): #Классово-базовове представление
    model = Place
    context_object_name = "place"
    template_name = "places.html"

def info(request, place_id): #Представление-функция через рендер реквеста
    try:
        a = Info.objects.get(id = place_id) #Берём внешний ключ из ссылки
    except:
        raise Http404("Объект не найден")
    return render(request, 'info.html', {'place' : a}) #Берём запрос, статик файл, далее передаём в шаблонизатор взятый выше id

    