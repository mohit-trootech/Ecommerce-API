from django.urls import path
from store.views import (
    store_home,
    create_product,
    cart_view,
    wishlist_view,
    view_product,
)
from utils.constants import Urls

urlpatterns = [
    path("", store_home, name=Urls.STORE.value),
    path("product/add", create_product, name=Urls.ADD_PRODUCT.value),
    path("cart", cart_view, name=Urls.CART.value),
    path("wishlist", wishlist_view, name=Urls.WISHLIST.value),
    path("product/<int:pk>", view_product, name=Urls.PRODUCT.value),
]
