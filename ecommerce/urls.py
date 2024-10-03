from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from schema_graph.views import Schema
from utils.constants import Urls
from rest_framework.routers import DefaultRouter
from ecommerce.views import (
    ProductViewSet,
    CategoryViewSet,
    CartViewSet,
    WishlistViewSet,
    OrderViewSet,
    index_view,
)
from accounts.views import UserViewSet


routers = DefaultRouter()
routers.register("products", ProductViewSet)
# routers.register("product_images", ProductImageViewSet)
routers.register("categories", CategoryViewSet)
routers.register("cart", CartViewSet)
routers.register("wishlist", WishlistViewSet)
routers.register("order", OrderViewSet)
routers.register("user", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("accounts/", include("accounts.urls")),
    path("schema", Schema.as_view(), name=Urls.SCHEMA_REVERSE.value),
    path("api/", include(routers.urls)),
] + debug_toolbar_urls()
