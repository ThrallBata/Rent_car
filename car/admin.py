from django.contrib import admin

from .models import *


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_car', 'year')
    search_fields = ('name_car', 'year')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'car')
    search_fields = ('car',)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Client, ClientAdmin)

