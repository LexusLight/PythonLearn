from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''def index(request):
    return HttpResponse("Hello world")'''

def index(request):
    return HttpResponse("You're looking at question.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


