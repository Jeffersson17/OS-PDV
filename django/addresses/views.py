from addresses.models import Address, City
from addresses.serializers import AddressSerializer, CitySerializer
from rest_framework import generics, viewsets


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by("id")
    serializer_class = AddressSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by("id")
    serializer_class = CitySerializer


class AddressDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
