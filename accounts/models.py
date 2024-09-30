from django.contrib.auth.models import AbstractUser
from django.db.models import UUIDField
from uuid import uuid4
from django_extensions.db.fields import CreationDateTimeField


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
