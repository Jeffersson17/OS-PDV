from addresses.models import Address, City
from addresses.serializers import AddressSerializer, CitySerializer
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
