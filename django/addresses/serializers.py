from addresses.models import Address, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    city_base = city_base = CitySerializer(read_only=True, source="city")

    class Meta:
        model = Address
        fields = "__all__"
