from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
