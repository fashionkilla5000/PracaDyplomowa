from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_restaurator = models.BooleanField(default=False)
    pass

    class Meta:
        ordering = ['date_joined']