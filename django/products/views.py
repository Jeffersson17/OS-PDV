from products.models import Product, ProductBrand
from products.serializers import ProductSerializer, SerializerProductBrand
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = SerializerProductBrand
