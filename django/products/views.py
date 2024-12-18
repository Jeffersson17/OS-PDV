from products.models import Product, ProductBrand
from products.serializers import ProductSerializer, SerializerProductBrand
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


class ProductBrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductBrand.objects.all().order_by("id")
    serializer_class = SerializerProductBrand


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductBrand.objects.all()
    serializer_class = SerializerProductBrand
