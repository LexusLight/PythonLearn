from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView,DetailView,View #Для создания класса 
from first.models import FromForm
from .forms import PostForm ##Для формы

def first(request): #Представление-функция через рендер реквеста
    a = FromForm.objects.all()
    b = PostForm()
    context = {
        'text': a,
        'form': b,
    }
    return render(request, 'first.html',context) #Берём запрос, статик файл, далее передаём в шаблонизатор взятый выше id


class PostObr(View):
    def post(self,request):
        form = PostForm(self.request.POST)
        if form.is_valid():
            post = FromForm(form_text = form.cleaned_data['text'])
            post.save()
        return HttpResponseRedirect('/first')
