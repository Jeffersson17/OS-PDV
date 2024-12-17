from rest_framework import generics, viewsets
from sales.models import ProductsSales, Sales
from sales.serializers import SerializerProductsSales, SerializerSales


class ProductsSalesViewSet(viewsets.ModelViewSet):
    queryset = ProductsSales.objects.all().order_by("id")
    serializer_class = SerializerProductsSales


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all().order_by("id")
    serializer_class = SerializerSales


class SalesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SerializerSales


class ProductsSalesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductsSales.objects.all()
    serializer_class = SerializerProductsSales
