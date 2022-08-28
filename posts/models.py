from django.db import models
from django.utils import timezone
from phone_field import PhoneField


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)

    no_of_likes = models.CharField(max_length=50, null = True, blank=True)

    adres = models.CharField(max_length=50, null = False)
    nr_domu = models.CharField(max_length=4, null = False, blank=True)

    choose_payment = (
        ('karta','Karta'),
        ('gotowka','Gotowka'),
        ('zaplacone','Zaplacone')
    )
    płatność = models.CharField(max_length=10, choices=choose_payment, default='zaplacone')

    kwota = models.CharField(max_length=5, null = False)
    telefon = models.CharField(max_length=13, null = False)
    komentarz = models.CharField(max_length=200, null=True, blank=True)

    choose_platform = (
        ('uber','Uber'),
        ('rest','Rest'),
        ('glovo','Glovo'),
        ('tel','Tel')
    )
    platforma = models.CharField(max_length=5, choices=choose_platform, default='glovo')

    oczekujace = models.BooleanField(default=True)
    trasa = models.BooleanField(default=False)
    zakonczone = models.BooleanField(default=False)

    def __str__(self):
        return self.adres

    class Meta:
        ordering = ['date']


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username