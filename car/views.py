from rest_framework import generics
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Client, Cars
from .forms import ClientForm
from .serializers import CarsSerializer


def index(request):
    error = ""
    if request.method == 'POST':
        filled_form = ClientForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()

        else:
            error = "Некорректно заполняна форма!"

    form = ClientForm()

    cars = Cars.objects.all()

    data = {
        'form': form,
        'error': error,
        'cars': cars
    }

    return render(request, 'car/index.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class CarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
