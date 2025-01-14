from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop("user_permissions", [])
        groups = validated_data.pop("groups", [])
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        instance.user_permissions.set(permissions)
        instance.groups.set(groups)
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
        instance.save()
        return instance
