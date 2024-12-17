import uuid

from products.models import Product

from django.db import models
from django.db.models import F, Sum
from django.utils import timezone


class Sales(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    purchase_date = models.DateField()
    products = models.ManyToManyField(
        Product, related_name="sale", through="ProductsSales"
    )
    created_date = models.DateTimeField(
        auto_now_add=True, default=timezone.now
    )

    def total_price(self):
        return (
            self.productssales_set.aggregate(
                total=Sum(F("quantity_purchased") * F("product__price"))
            )["total"]
            or 0
        )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"


class ProductsSales(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    quantity_purchased = models.PositiveIntegerField()
    created_date = models.DateTimeField(
        auto_now_add=True, default=timezone.now
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity_purchased}"

    def check_stock(self):
        if self.quantity_purchased > self.product.stock:
            raise ValueError(
                f"Estoque insuficiente para {self.product.name}. "
                f"Disponível: {self.product.stock}, solicitado: {self.quantity_purchased}."
            )
        self.product.stock -= self.quantity_purchased
        self.product.save()

    def total_price(self):
        total_price = self.product.price * self.quantity_purchased
        return total_price

    def save(self, *args, **kwargs):
        self.check_stock()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Produto Vendido"
        verbose_name_plural = "Produtos Vendidos"
