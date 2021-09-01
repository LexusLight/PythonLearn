from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import FromForm
from django.views.generic import View
from .forms import PostForm ##Для формы

def first(request): #Представление-функция через рендер реквеста
    a = FromForm.objects.all().order_by("-id")
    b = PostForm()
    context = {
        'text': a,
        'form': b,
    }
    return render(request, 'first.html',context) #Берём запрос, статик файл, далее передаём в шаблонизатор взятый выше id


def post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = FromForm(form_text = form.cleaned_data['text'])
        post.save()
    return HttpResponseRedirect('/B')