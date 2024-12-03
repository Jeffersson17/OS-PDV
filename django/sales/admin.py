from django.contrib import admin

from sales.models import ProductsSales, Sales

admin.site.register(Sales)
admin.site.register(ProductsSales)
