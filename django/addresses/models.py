import uuid

from django.db import models


class City(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    address = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    complement = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
