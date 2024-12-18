from addresses.models import Address, City
from addresses.serializers import AddressSerializer, CitySerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all().order_by("id")
    serializer_class = AddressSerializer


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all().order_by("id")
    serializer_class = CitySerializer


class AddressDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
