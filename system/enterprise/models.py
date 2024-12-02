from django.db import models
from address.models import Address
from django.contrib.auth.models import AbstractUser


class Enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    area = models.CharField(max_length=75)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class CustomUser(AbstractUser):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField()


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
