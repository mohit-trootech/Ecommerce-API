from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)


class CartWishlistAbstract(models.Model):
    user = models.OneToOneField(
        "auth.User", on_delete=models.CASCADE, related_name="%(class)s"
    )
    products = models.ManyToManyField(
        "Product", blank=True, related_name="%(class)s_items"
    )

    @property
    def get_total_price(self):
        return sum([product.price for product in self.products.all()])

    @property
    def get_total_tax(self):
        return (self.get_total_price * 18) / 100

    @property
    def get_grand_total(self):
        return self.get_total_price + self.get_total_tax

    get_total_price.fget.short_description = "Total Price"
    get_total_tax.fget.short_description = "Total Tax"
    get_grand_total.fget.short_description = "Grand Total"

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Cart(CartWishlistAbstract):

    def __str__(self):
        return "{user}'s Cart".format(user=self.user.username).capitalize()


class Wishlist(CartWishlistAbstract):

    def __str__(self):
        return "{user}'s Wishlist".format(user=self.user.username).capitalize()


class Category(TitleDescriptionModel):

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    class Meta:
        ordering = ["?"]

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.URLField(max_length=1024)


class ApiStats(models.Model):
    hit = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.hit)
