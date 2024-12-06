from products.models import Product

from django.db import models


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    purchase_date = models.DateField()
    products = models.ManyToManyField(
        Product, related_name="sale", through="ProductsSales"
    )

    def total_price(self):
        total = 0
        for product_sale in self.productssales_set.all():
            total += product_sale.total_price()
        return total

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"


class ProductsSales(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    quantity_purchased = models.PositiveIntegerField()

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
        verbose_name = "Produto Vendido"
        verbose_name_plural = "Produtos Vendidos"
