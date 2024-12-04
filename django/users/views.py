from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
