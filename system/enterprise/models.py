from django.db import models
from address.models import Address


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


class User(models.Model):
    id = models.AutoField(primary_key=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField()
    email = models.EmailField()


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
