from enterprises.models import Enterprise

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
