from addresses.views import (
    AddressDetailAPIView,
    AddressViewSet,
    CityDetailAPIView,
    CityViewSet,
)
from products.views import (
    ProductBrandDetailAPIView,
    ProductBrandListAPIView,
    ProductBrandViewSet,
    ProductDetailAPIView,
    ProductListAPIView,
    ProductViewSet,
)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from sales.views import (
    ProductsSalesDetailAPIView,
    ProductsSalesListAPIView,
    ProductsSalesViewSet,
    SalesDetailAPIView,
    SalesListAPIView,
    SalesViewSet,
)
from users.views import UserDetailAPIView, UserViewSet

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
    path(
        "users-api/detail/<int:pk>/",
        UserDetailAPIView.as_view(),
        name="detail_api",
    ),
    path("sales-api/list/", SalesListAPIView.as_view(), name="sales_list"),
    path(
        "sales-api/detail/<int:pk>/",
        SalesDetailAPIView.as_view(),
        name="sales_detail",
    ),
    path(
        "products-sales/list/",
        ProductsSalesListAPIView.as_view(),
        name="products_sales_list",
    ),
    path(
        "products-sales/detail/<int:pk>/",
        ProductsSalesDetailAPIView.as_view(),
        name="products_sales_detail",
    ),
    path(
        "address-api/detail/<int:pk>/",
        AddressDetailAPIView.as_view(),
        name="address_detail",
    ),
    path(
        "city-api/detail/<int:pk>/",
        CityDetailAPIView.as_view(),
        name="city_detail",
    ),
    path(
        "product-api/list/", ProductListAPIView.as_view(), name="product_list"
    ),
    path(
        "product-brand-api/list/",
        ProductBrandListAPIView.as_view(),
        name="product_brand_list",
    ),
    path(
        "product-api/detail/<int:pk>/",
        ProductDetailAPIView.as_view(),
        name="product_detail",
    ),
    path(
        "product-brand-api/detail/<int:pk>/",
        ProductBrandDetailAPIView.as_view(),
        name="product_brand_detail",
    ),
]
