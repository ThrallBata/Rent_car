from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from .models import Client, Cars
from .forms import ClientForm
from .serializers import CarsSerializer


menu = [{'title': "Главная", 'id': 'menu-home'},
        {'title': "Автомобили", 'id': 'menu-car'},
        {'title': "Бронирование авто", 'id': 'menu-price'}]


def index(request):
    error = ""
    succes_record = ''
    if request.method == 'POST':
        if save_and_validate_client_form(ClientForm(request.POST)):
            return redirect('success')
        else:
            error = "Некорректно заполняна форма!"

    form = ClientForm()
    cars = Cars.objects.all()

    data = {
        'form': form,
        'error': error,
        'cars': cars,
        'succes_record': succes_record,
        'menu': menu,
    }

    return render(request, 'car/index.html', data)


def success_form(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'car/success_form.html')


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


def save_and_validate_client_form(client_form):
    if _validate_client_form(client_form):
        client_form.save()
        return True
    return False


def _validate_client_form(client_form):
    if client_form.is_valid():
        return True


