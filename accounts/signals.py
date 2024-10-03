from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User
from ecommerce.models import Cart, Wishlist, Order


@receiver(post_save, sender=User)
def create_user_cart_wishlist(sender, instance, created, **kwargs):
    if created:

        Cart.objects.create(user=instance)
        Wishlist.objects.create(user=instance)


@receiver(post_save, sender=Order)
def empty_user_cart_post_order_create(sender, instance, created, *args, **kwargs):
    if created:
        cart = Cart.objects.get(user=instance.user)
        cart.products.clear()
        cart.save()
