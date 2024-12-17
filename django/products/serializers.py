from products.models import Product, ProductBrand
from rest_framework import serializers


class SerializerProductBrand(serializers.ModelSerializer):

    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    enterprise_name = serializers.StringRelatedField(source="enterprise")
    mark_name = serializers.StringRelatedField(source="mark")

    class Meta:
        model = Product
        fields = "__all__"
