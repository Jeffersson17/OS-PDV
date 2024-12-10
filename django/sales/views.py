from rest_framework import viewsets
from sales.models import ProductsSales, Sales
from sales.serializers import SerializerProductsSales, SerializerSales


class ProductsSalesViewSet(viewsets.ModelViewSet):
    queryset = ProductsSales.objects.all()
    serializer_class = SerializerProductsSales


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SerializerSales
