from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from utils.constants import ModelChoices


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        choices=ModelChoices.GENDER_CHOICE.value, null=True, blank=True, max_length=1
    )
    phone = PhoneNumberField(region="IN", blank=True, null=True)

    def __str__(self):
        return self.username
