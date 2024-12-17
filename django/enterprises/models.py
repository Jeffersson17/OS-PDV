import uuid

from addresses.models import Address

from django.db import models


class Enterprise(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    name = models.CharField(max_length=150)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    area = models.CharField(max_length=75)
    created_date = models.DateTimeField(
        auto_now_add=True, editable=False
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
