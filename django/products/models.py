import uuid

from enterprises.models import Enterprise

from django.db import models


class ProductBrand(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Marca do Produto"


class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    mark = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
