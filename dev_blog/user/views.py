from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    return HttpResponse('Hola mundo desde Django')


def register(request):
    return HttpResponse('Hola mundo, registrate')