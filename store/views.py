from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from utils.constants import Templates
from store.forms import CreateProductForm


class StoreHome(TemplateView):
    template_name = Templates.STORE.value


store_home = StoreHome.as_view()


class CreateProduct(TemplateView):
    template_name = Templates.PRODUCT_ADD.value

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = CreateProductForm()
        return context


create_product = CreateProduct.as_view()


class ViewProduct(TemplateView):
    template_name = Templates.PRODUCT.value


view_product = ViewProduct.as_view()


class CartView(TemplateView):
    template_name = Templates.CART.value


cart_view = CartView.as_view()


class WishlistView(TemplateView):
    template_name = Templates.WISHLIST.value


wishlist_view = WishlistView.as_view()
