from django.db import models
from django.core.validators import RegexValidator


class Cars(models.Model):
    name_car = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    enginе = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.name_car


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_Number_Regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_Number_Regex], max_length=12, unique=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)

