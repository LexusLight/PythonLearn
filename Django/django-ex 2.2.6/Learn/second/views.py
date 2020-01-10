from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View #Для создания класса 
from .models import User, Message
from .forms import UserForm
x = 2
# Create your views here.
def reg(request):
    if(x == 2):
        user = User.objects.get(username="admin")
        return render(request, 'user.html', {"user":user})
    else:
        form = UserForm()
        return render(request, 'reg.html', {"form":form})

def exit(request):
    user = User.objects.get(username="admin")
    form = UserForm()
    return render(request, 'reg.html', {"form":form})

class RegObr(View):
    def post(self,request):
        form = UserForm(self.request.POST)
        if form.is_valid():
            user = User(username = form.cleaned_data['username'],realname = form.cleaned_data['realname'])
            user.save()
        return HttpResponseRedirect('/second')
    