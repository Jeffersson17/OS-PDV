from addresses.views import AddressViewSet, CityViewSet
from products.views import ProductBrandViewSet, ProductViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from sales.views import ProductsSalesViewSet, SalesViewSet
from users.views import UserDetailAPIView, UserListAPIView, UserViewSet

from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"address", AddressViewSet)
router.register(r"city", CityViewSet)
router.register(r"product", ProductViewSet)
router.register(r"product_brand", ProductBrandViewSet)
router.register(r"products_sales", ProductsSalesViewSet)
router.register(r"sales", SalesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path("users-api/list/", UserListAPIView.as_view(), name="list_api"),
    path(
        "users-api/detail/<int:pk>/",
        UserDetailAPIView.as_view(),
        name="detail_api",
    ),
]
