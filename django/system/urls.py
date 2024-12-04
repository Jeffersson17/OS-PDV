from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserViewSet

from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
