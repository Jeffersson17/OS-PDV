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
