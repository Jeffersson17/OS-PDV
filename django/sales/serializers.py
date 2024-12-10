from rest_framework import serializers
from sales.models import ProductsSales, Sales


class SerializerSales(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source="user")
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = [
            "id",
            "user",
            "username",
            "purchase_date",
            "total_price",
            "products",
        ]

    def get_total_price(self, obj):
        return obj.total_price()


class SerializerProductsSales(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField(source="product")

    class Meta:
        model = ProductsSales
        fields = [
            "id",
            "product",
            "product_name",
            "sale",
            "quantity_purchased",
        ]
