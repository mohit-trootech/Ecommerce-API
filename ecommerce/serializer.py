from rest_framework import serializers, status, exceptions
from ecommerce.models import Product, Cart, ProductImages, Wishlist, Category, Order
from django.db.utils import IntegrityError
from uuid import uuid4


class CustomModelSerializer(serializers.ModelSerializer):

    def get_products_initial_data(self):
        products = self.initial_data.get("products") or None
        if products is None:
            raise exceptions.APIException(
                "Products are required", status.HTTP_400_BAD_REQUEST
            )
        if isinstance(products, str):
            products = eval(products)
        return products

    def update(self, instance, validated_data):
        products = self.get_products_initial_data()
        instance.products.set(products)
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
            raise exceptions.APIException(
                "Category Does not exist with The Given Id",
                status.HTTP_400_BAD_REQUEST,
            )

    @staticmethod
    def create_images_instances(images, instance):
        try:
            ProductImages.objects.bulk_create(
                [ProductImages(product=instance, image=image) for image in eval(images)]
            )
        except Exception as err:
            raise exceptions.APIException(err, status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_images_instances(product):
        try:
            return ProductImages.objects.filter(product__id=product.id)
        except Exception as err:
            raise exceptions.APIException(err, status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        instance = Product(**validated_data)
        category = self.get_category_instance(self.initial_data.get("category", None))
        instance.category = category
        if self.initial_data.get("images"):
            instance.save()
            self.create_images_instances(self.initial_data.get("images"), instance)
            return instance
        raise exceptions.APIException(
            "Images are required", status.HTTP_400_BAD_REQUEST
        )

    def update(self, instance, validated_data):
        if self.initial_data.get("category"):
            instance.category = self.get_category_instance(
                id=self.initial_data.get("category")
            )
        if self.initial_data.get("images"):
            print(instance.images.all())
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
            raise exceptions.APIException(
                "Products Does not exist with The Given Id", status.HTTP_400_BAD_REQUEST
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
            raise exceptions.APIException(
                "Products Does not exist with The Given Id", status.HTTP_400_BAD_REQUEST
            )


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        read_only_fields = [
            "id",
            "user",
            "get_total_price",
            "get_total_tax",
            "get_grand_total",
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
            raise exceptions.APIException(
                "Products Does not exist with The Given Id", status.HTTP_400_BAD_REQUEST
            )
