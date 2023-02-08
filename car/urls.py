from django.urls import path

from .views import *

#app_name = 'car'

urlpatterns = [
    path('', index, name='home'),
    path('success/', success_form, name='success'),
]
