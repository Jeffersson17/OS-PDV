from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from sales.models import ProductsSales, Sales
from sales.serializers import SerializerProductsSales, SerializerSales


class ProductsSalesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductsSales.objects.all().order_by("id")
    serializer_class = SerializerProductsSales


class SalesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Sales.objects.all().order_by("id")
    serializer_class = SerializerSales


class SalesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sales.objects.all()
    serializer_class = SerializerSales


class ProductsSalesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductsSales.objects.all()
    serializer_class = SerializerProductsSales
