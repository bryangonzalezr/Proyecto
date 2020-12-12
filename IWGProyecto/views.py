from django import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def plantilla(request):
    return render(request, 'Plantilla1.html')

def juego(request):
    return render(request, 'index.html')


    