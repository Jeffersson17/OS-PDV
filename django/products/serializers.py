from products.models import Product, ProductBrand
from rest_framework import serializers


class SerializerProductBrand(serializers.ModelSerializer):

    class Meta:
        model = ProductBrand
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    enterprise_name = serializers.StringRelatedField(source="enterprise")
    mark_name = serializers.StringRelatedField(source="mark")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "enterprise",
            "enterprise_name",
            "mark",
            "mark_name",
            "stock",
        ]
