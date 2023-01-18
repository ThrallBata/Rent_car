from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
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


def about_car(request):
    data = {
        'form': form,
        'error': error,
        'cars': cars
    }

    return render(request, 'car/base.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class CarsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    #queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Cars.objects.all()[:]

        return Cars.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def client(self, request, pk=None):
        client = Client.objects.get(pk=pk)
        return Response({'client': client.name})


