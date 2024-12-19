from addresses.views import (
    AddressDetailAPIView,
    AddressViewSet,
    CityDetailAPIView,
    CityViewSet,
)
from products.views import (
    ProductBrandDetailAPIView,
    ProductBrandViewSet,
    ProductDetailAPIView,
    ProductViewSet,
)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from sales.views import (
    ProductsSalesDetailAPIView,
    ProductsSalesViewSet,
    SalesDetailAPIView,
    SalesViewSet,
)
from users.views import UserDetailAPIView, UserViewSet

from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"cities", CityViewSet)
router.register(r"products", ProductViewSet)
router.register(r"products_brands", ProductBrandViewSet)
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
    path(
        "users/user/<uuid:pk>/",
        UserDetailAPIView.as_view(),
        name="detail_api",
    ),
    path(
        "sales/sale/<uuid:pk>/",
        SalesDetailAPIView.as_view(),
        name="sales_detail",
    ),
    path(
        "products_sales/product_sale/<uuid:pk>/",
        ProductsSalesDetailAPIView.as_view(),
        name="products_sales_detail",
    ),
    path(
        "addresses/address/<uuid:pk>/",
        AddressDetailAPIView.as_view(),
        name="address_detail",
    ),
    path(
        "cities/city/<uuid:pk>/",
        CityDetailAPIView.as_view(),
        name="city_detail",
    ),
    path(
        "products/product/<uuid:pk>/",
        ProductDetailAPIView.as_view(),
        name="product_detail",
    ),
    path(
        "products_brands/product_brand/<uuid:pk>/",
        ProductBrandDetailAPIView.as_view(),
        name="product_brand_detail",
    ),
]
