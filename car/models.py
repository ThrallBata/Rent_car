from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Cars(models.Model):
    name_car = models.CharField(max_length=50, verbose_name='Машина')
    transmission = models.CharField(max_length=50)
    enginе = models.CharField(max_length=10)
    year = models.CharField(max_length=4, verbose_name="Год")

    def __str__(self):
        return self.name_car

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Машины в наличии'
        verbose_name_plural = 'Машины в наличии'
        ordering = ['name_car']


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone_Number_Regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_Number_Regex], max_length=12, unique=True, verbose_name='Номер телефона')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name='Машина')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'
        ordering = ['car']
