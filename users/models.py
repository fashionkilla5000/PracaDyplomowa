from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Restauracja


class CustomUser(AbstractUser):
    choose_stanowisko = (
        ('Driver', 'Driver'),
        ('Restaurator', 'Restaurator')
    )
    stanowisko = models.CharField(max_length=50, choices=choose_stanowisko, default='Driver')
    restaurant = models.ForeignKey(Restauracja, on_delete=models.CASCADE, null=True)
    pass

    class Meta:
        ordering = ['date_joined']


