from django.contrib import admin

from products.models import Product, ProductBrand

admin.site.register(Product)
admin.site.register(ProductBrand)
