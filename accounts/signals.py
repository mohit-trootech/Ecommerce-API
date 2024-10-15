from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ecommerce.models import Cart, Wishlist


@receiver(post_save, sender=User)
def create_user_cart_wishlist(sender, instance, created, **kwargs):
    if created:

        Cart.objects.create(user=instance)
        Wishlist.objects.create(user=instance)
