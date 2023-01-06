from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Client


def index(request):
    return render(request, 'car/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
