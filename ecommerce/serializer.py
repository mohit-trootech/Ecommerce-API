from rest_framework import serializers, status, exceptions
from ecommerce.models import Product, Cart, ProductImages, Wishlist, Category, Order
from django.db.utils import IntegrityError
from uuid import uuid4
from utils.constants import SerializersConstants, OperationType


class CustomModelSerializer(serializers.ModelSerializer):

    def get_products_initial_data(self):
        products = self.initial_data.get("products") or None
        if products is None:
            raise exceptions.NotFound(
                SerializersConstants.PRODUCTS_REQUIRED.value,
            )
        if isinstance(products, str):
            products = eval(products)
        return products

    def get_product_from_query_params(self):
        product = self.context.get("request").query_params.get("product") or None
        if product is None:
            raise exceptions.NotFound(
                SerializersConstants.PRODUCTS_REQUIRED.value,
            )
        return product

    def operation_type(self):
        operation = self.context.get("request").query_params.get("operation") or None
        if operation is None:
            raise exceptions.NotFound(
                SerializersConstants.OPERATION_REQUIRED.value,
            )
        return operation

    def update(self, instance, validated_data):
        operation = self.operation_type()
        if operation == OperationType.ADD.value:
            product = self.get_product_from_query_params()
            if isinstance(product, str):
                product = eval(product)
            instance.products.add(product)
            instance.save()
        elif operation == OperationType.REMOVE.value:
            product = self.get_product_from_query_params()
            if isinstance(product, str):
                product = eval(product)
            instance.products.remove(product)
            instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    @staticmethod
    def get_category_instance(id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise exceptions.NotFound(
                SerializersConstants.CATEGORY_NOT_EXIST.value,
            )

    @staticmethod
    def create_images_instances(images, instance):
        try:
            ProductImages.objects.bulk_create(
                [ProductImages(product=instance, image=image) for image in eval(images)]
            )
        except Exception as err:
            raise exceptions.APIException(err, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_images_instances(product):
        try:
            return ProductImages.objects.filter(product__id=product.id)
        except Exception as err:
            raise exceptions.APIException(err, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, validated_data):
        instance = Product(**validated_data)
        category = self.get_category_instance(self.initial_data.get("category", None))
        instance.category = category
        if self.initial_data.get("images"):
            instance.save()
            self.create_images_instances(self.initial_data.get("images"), instance)
            return instance
        raise exceptions.APIException(
            SerializersConstants.IMAGES_REQUIRED.value, status.HTTP_400_BAD_REQUEST
        )

    def update(self, instance, validated_data):
        if self.initial_data.get("category"):
            instance.category = self.get_category_instance(
                id=self.initial_data.get("category")
            )
        if self.initial_data.get("images"):
            instance.images.all().delete()
            self.create_images_instances(self.initial_data.get("images"), instance)
        return super().update(instance, validated_data)


class OrderSerializer(CustomModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        read_only_fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
        ]
        fields = "__all__"

    def create(self, validated_data):
        products = self.get_products_initial_data()

        order = Order.objects.create(id=uuid4(), user=self.context["request"].user)
        try:
            order.products.add(*products)
            order.save()
            return order
        except IntegrityError:
            order.delete()
            raise exceptions.NotFound(
                SerializersConstants.PRODUCT_NOT_EXIST.value,
            )


class CartSerializer(CustomModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        read_only_fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
            "products",
        ]
        fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
            "products",
        ]

    def create(self, validated_data):
        products = self.get_products_initial_data()
        cart = Cart.objects.get(user=self.context["request"].user)
        try:
            cart.products.add(*products)
            cart.save()
            return cart
        except IntegrityError:
            raise exceptions.NotFound(
                SerializersConstants.PRODUCT_NOT_EXIST.value,
            )


class WishlistSerializer(CustomModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        read_only_fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
            "products",
        ]
        fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
            "products",
        ]

    def create(self, validated_data):
        products = self.get_products_initial_data()
        wishlist = Wishlist.objects.get(user=self.context["request"].user)
        try:
            wishlist.products.add(*products)
            wishlist.save()
            return wishlist
        except IntegrityError:
            raise exceptions.NotFound(
                SerializersConstants.PRODUCT_NOT_EXIST.value,
            )
