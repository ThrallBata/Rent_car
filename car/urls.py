from django.urls import path

from .views import *

app_name = 'car'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_car, name='about'),
]
