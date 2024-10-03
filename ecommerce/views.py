from rest_framework import viewsets, mixins
from ecommerce.models import Product, Category, ProductImages, Cart, Wishlist, Order
from ecommerce.serializer import (
    ProductSerializer,
    CategorySerializer,
    CartSerializer,
    WishlistSerializer,
    OrderSerializer,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from utils.constants import EMPTY_STR
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "ecommerce/index.html"


index_view = IndexView.as_view()


class CustomUserFilterViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    def get_queryset(self):
        user = self.request.query_params.get("user") or None
        if user is None:
            return super().get_queryset()
        return self._model_name.objects.filter(user__username=user)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("images").all()
    )
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CartViewSet(CustomUserFilterViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    _model_name = Cart


class WishlistViewSet(CustomUserFilterViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    _model_name = Wishlist


class OrderViewSet(CustomUserFilterViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    _model_name = Order
