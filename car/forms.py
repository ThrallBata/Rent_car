from django.core.exceptions import ValidationError

from .models import Client, Cars
from django.forms import ModelForm, TextInput, Select


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].empty_label = "Автомобиль не выбран"

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
                "class": "price-input"
            })
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number[0] != '+' and phone_number[1] != '7':
            raise ValidationError('Некорректный номер телефона')

        return phone_number

