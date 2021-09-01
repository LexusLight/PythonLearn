from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from A.models import Pages

def menulist(request):

    try:
        a = Pages.objects.all()
    except:
        raise Http404("Pages not found")
    return render(request, 'menu.html',{'pages': a})