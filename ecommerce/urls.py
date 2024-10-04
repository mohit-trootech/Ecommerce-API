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
    about_view,
    terms_view,
)
from accounts.views import UserViewSet


routers = DefaultRouter()
routers.register("products", ProductViewSet)
routers.register("categories", CategoryViewSet)
routers.register("cart", CartViewSet)
routers.register("wishlist", WishlistViewSet)
routers.register("order", OrderViewSet)
routers.register("user", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name=Urls.HOME.value),
    path("about/", about_view, name=Urls.ABOUT.value),
    path("terms/", terms_view, name=Urls.TERMS.value),
    path("accounts/", include("accounts.urls")),
    path("store/", include("store.urls")),
    path("schema", Schema.as_view(), name=Urls.SCHEMA_REVERSE.value),
    path("api/", include(routers.urls), name=Urls.API_REVERSE.value),
] + debug_toolbar_urls()
