import uuid

from enterprises.models import Enterprise

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE, null=True, blank=True
    )
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, editable=False
    )

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
