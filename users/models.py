from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    choose_stanowisko = (
        ('Driver', 'Driver'),
        ('Restaurator', 'Restaurator')
    )
    stanowisko = models.CharField(max_length=50, choices=choose_stanowisko, default='Driver')
    choose_restauracja = (
        ('Joe Gonzalez', 'Joe Gonzalez'),
        ('Czeska Gospoda', 'Czeska Gospoda'),
        ('Mexicana', 'Mexicana')
    )
    restauracja = models.CharField(max_length=50, choices=choose_restauracja, default='Joe')
    pass

    class Meta:
        ordering = ['date_joined']