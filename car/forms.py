from .models import Client, Cars
from django.forms import ModelForm, TextInput, Select


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'car']

        widgets = {
            'name': TextInput(attrs={
                "class": "price-input",
                "placeholder": "Ваше имя"
        }),
            'phone_number': TextInput(attrs={
                "class": "price-input",
                "placeholder": "Ваш телефон"
            }),
            'car': Select(attrs={
                "class": "price-input",
                "placeholder": "Автомобиль, который вас интересует"
            })
        }
