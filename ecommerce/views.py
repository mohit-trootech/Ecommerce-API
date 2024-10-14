from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from rest_framework import viewsets, mixins
from ecommerce.models import Product, Category, Cart, Wishlist
from ecommerce.serializer import (
    ProductSerializer,
    CategorySerializer,
    CartSerializer,
    WishlistSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from utils.constants import EMPTY_STR, Templates
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from typing import Any
from utils.utils import get_repository_star, get_api_stats, StandardResultsSetPagination
from django.db.models import Q
from django.contrib.messages import info


class IndexView(TemplateView):
    template_name = Templates.INDEX.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["count"] = User.objects.count()
        context["star"] = get_repository_star()
        context["hit"] = get_api_stats()
        return context


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        info(
            request,
            "Please Test all the GET request <a class='text-secondary' href='/#api-Example'>Here</a>",
        )
        return super().get(request, *args, **kwargs)


about_view = AboutView.as_view()


class TermsView(TemplateView):
    template_name = Templates.TERMS.value


terms_view = TermsView.as_view()


@method_decorator(csrf_exempt, name="dispatch")
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        filter_params = self.request.query_params

        query = Q()
        if filter_params.get("category"):
            query = query & Q(category__title=filter_params.get("category"))
        return (
            super()
            .get_queryset()
            .filter(query)
            .order_by(
                filter_params.get("orderby") if filter_params.get("orderby") else "?"
            )
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


@method_decorator(csrf_exempt, name="dispatch")
class CartViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "user__username"


@method_decorator(csrf_exempt, name="dispatch")
class WishlistViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    lookup_field = "user__username"
