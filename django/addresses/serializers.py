from addresses.models import Address, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ["name", "state"]


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ["id", "address", "city", "cep", "number", "complement"]
