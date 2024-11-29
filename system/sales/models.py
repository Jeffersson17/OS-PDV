from django.db import models
from products.models import Product
from enterprise.models import User


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    products = models.ManyToManyField(Product, related_name='sale', through='ProductsSales')


class ProductsSales(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    quantity_purchased = models.DecimalField(max_digits=10, decimal_places=2)
