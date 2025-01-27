# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 2')

def contato(request):
    return HttpResponse('contato 40')

def sobre(request):
    return HttpResponse('sobre 30')