from rest_framework import serializers
from sales.models import ProductsSales, Sales
from products.models import Product


class SerializerSales(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),
        many=True
    )
    username = serializers.StringRelatedField(source="user")
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = ["id", "user_id", "username", "purchase_date", "total_price", "products"]

    def get_total_price(self, obj):
        return obj.total_price()


class SerializerProductsSales(serializers.ModelSerializer):

    class Meta:
        model = ProductsSales
        fields = ["id", "product", "sale", "quantity_purchased"]
