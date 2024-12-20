from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissions
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer
