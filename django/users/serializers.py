from users.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'is_staff',
            'phone_number',
            'cpf',
            'date_birth'
        ]
