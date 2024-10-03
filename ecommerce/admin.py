from django.contrib import admin
from .models import Cart, Wishlist, Category, Product, ProductImages, Order


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1


admin.register(ProductImages)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "created",
        "modified",
    ]
    list_display = ("id", "title", "price", "stock", "category")
    search_fields = ("title",)
    list_filter = ("category",)
    inlines = [ProductImagesInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    readonly_fields = ["id"]
    fieldsets = (
        (
            None,
            {
                "fields": ("id", "title", "description"),
            },
        ),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "get_total_price",
        "get_total_tax",
        "get_grand_total",
    ]
    list_display = ("id", "user", "get_grand_total")
    search_fields = ("user__username",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "user",
                    "products",
                ),
            },
        ),
        (
            "Meta Data",
            {
                "fields": (
                    "get_total_price",
                    "get_total_tax",
                    "get_grand_total",
                ),
            },
        ),
    )
    filter_horizontal = ("products",)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "get_total_price",
        "get_total_tax",
        "get_grand_total",
    ]
    list_display = ("id", "user", "get_grand_total")
    search_fields = ("user__username",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "user",
                    "products",
                ),
            },
        ),
        (
            "Meta Data",
            {
                "fields": (
                    "get_total_price",
                    "get_total_tax",
                    "get_grand_total",
                ),
            },
        ),
    )
    filter_horizontal = ("products",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "created",
        "modified",
        "get_total_price",
        "get_total_tax",
        "get_grand_total",
    ]
    list_display = ("id", "user", "created", "get_grand_total")
    search_fields = ("id",)
    list_filter = ["created"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "user",
                    "products",
                    "created",
                    "modified",
                ),
            },
        ),
        (
            "Meta Data",
            {
                "fields": (
                    "get_total_price",
                    "get_total_tax",
                    "get_grand_total",
                ),
            },
        ),
    )
    filter_horizontal = ("products",)
