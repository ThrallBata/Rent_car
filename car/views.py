from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Client


def index(request):
    return render(request, 'car/index.html')
