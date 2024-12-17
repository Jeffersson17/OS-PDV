from products.models import Product, ProductBrand
from products.serializers import ProductSerializer, SerializerProductBrand
from rest_framework import generics, viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all().order_by("id")
    serializer_class = SerializerProductBrand


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = SerializerProductBrand
