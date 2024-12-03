from products.models import Product

from django.db import models


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    purchase_date = models.DateField()
    products = models.ManyToManyField(
        Product, related_name="sale", through="ProductsSales"
    )

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"


class ProductsSales(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    quantity_purchased = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Produto Vendido"
        verbose_name_plural = "Produtos Vendidos"
