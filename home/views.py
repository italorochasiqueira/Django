from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('home')
    return HttpResponse('Você acessou a HOME do App!')

