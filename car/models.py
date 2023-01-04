from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_Number_Regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_Number_Regex], max_length=11, unique=True)

