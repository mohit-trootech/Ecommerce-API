from rest_framework import serializers
from ecommerce.models import Product, Cart, ProductImages, Wishlist, Category
from utils.constants import OperationType
from accounts.serializer import BaseCartWishlistUserSerializer


class DynamicModelFieldSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class RequiredParams(serializers.Serializer):
    product = serializers.CharField(
        required=True,
        allow_null=False,
    )
    operation = serializers.ChoiceField(
        choices=[i.value for i in OperationType],
        required=True,
    )

    def validate(self, attrs):
        try:
            product = Product.objects.get(id=attrs["product"])
        except Product.DoesNotExist:
            raise serializers.ValidationError("Invalid product id")
        attrs["product"] = product
        return attrs


class CustomModelSerializer(DynamicModelFieldSerializer):

    def update(self, instance, validated_data):
        serializer = RequiredParams(data=self.context.get("request").query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        operation = data["operation"]
        product = data["product"]
        if operation == OperationType.ADD.value:
            instance.products.add(product.id)
            instance.save()
        elif operation == OperationType.REMOVE.value:
            instance.products.remove(product.id)
            instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "description"]


class ProductImageSerializer(DynamicModelFieldSerializer):
    class Meta:
        model = ProductImages
        fields = ["id", "image"]


class ProductSerializerBase(DynamicModelFieldSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "description", "images"]


class ProductSerializer(ProductSerializerBase):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "stock",
            "category",
            "images",
            "created",
        ]
        depth = True

    def create(self, validated_data):
        instance = super().create(validated_data)
        images = self.initial_data.get("images")
        if images:
            images = eval(images) if isinstance(images, str) else images
            serializer = ProductImageSerializer(
                data=[{"product": instance.id, "image": i} for i in images],
                many=True,
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        images = self.initial_data.get("images")
        if images:
            images = eval(images) if isinstance(images, str) else images
            for image_data in images:
                try:
                    image = ProductImages.objects.get(id=image_data["id"])
                    serializer = ProductImageSerializer(image, data=image_data)
                except ProductImages.DoesNotExist:
                    serializer = ProductImageSerializer(
                        data={"product": instance.id, "image": image_data["image"]}
                    )
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return instance


class CartSerializer(CustomModelSerializer):
    products = ProductSerializerBase(many=True, read_only=True)
    user = BaseCartWishlistUserSerializer(read_only=True)

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
        extra_kwargs = {"products": {}}


class WishlistSerializer(CustomModelSerializer):
    products = ProductSerializerBase(many=True, read_only=True)
    user = BaseCartWishlistUserSerializer(read_only=True)

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
        depth = 1
