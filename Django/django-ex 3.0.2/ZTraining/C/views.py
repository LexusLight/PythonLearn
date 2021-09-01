from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpResponsePermanentRedirect, HttpRequest
from django.views.generic import View #Для создания класса 
from .models import User, Message
from .forms import UserForm
# Create your views here.
def reg(request):

    # if request.COOKIES is not None:
    #     x = request.COOKIES.get("x")
    # else:
    #     x = 2
    
    # x = 2
    if 'x' in request.session and 'username' in request.session:
        x = request.session['x']
    else:
        x = 2

    if(x == 1):
        username = request.session['username']
        user = User.objects.get(username = username)
        return render(request, 'user.html', {"user":user})
        
    elif(x == 2):
        form = UserForm()
        return render(request, 'reg.html', {"form":form})

def exit(request):

    resp = HttpResponsePermanentRedirect('/C')
    # resp.set_cookie('x',2)
    del request.session['x']
    request.session['x'] = 2
    del request.session['username']
    return resp

def post(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = User(username = form.cleaned_data['username'],realname = form.cleaned_data['realname'])
        user.save()
        resp = HttpResponseRedirect('/C') #Задаём куки. Пока не работает.
        # resp.set_cookie('x',1,max_age=10000)
        request.session['x'] = 1
        request.session['username'] = form.cleaned_data['username']
        return resp

    else:
        return HttpResponseRedirect('/C')

