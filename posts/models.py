from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now,editable=False)
    adres = models.CharField(max_length=50, null = False)

    choose_payment = (
        ('karta','Karta'),
        ('gotowka','Gotowka'),
        ('zaplacone','Zaplacone')
    )
    payment = models.CharField(max_length=10, choices=choose_payment, default='zaplacone')

    amount = models.CharField(max_length=5, null = False)
    phone = models.CharField(max_length=12)
    comment = models.CharField(max_length=200, null=True, blank=True)

    choose_platform = (
        ('uber','Uber'),
        ('rest','Rest'),
        ('glovo','Glovo'),
        ('tel','Tel')
    )
    platform = models.CharField(max_length=5, choices=choose_platform, default='glovo')

    choose_status = (
        ('oczekujacy','Oczekujacy'),
        ('w trakcie', 'W trakcie'),
        ('zakonczony','Zakonczony')
    )
    status = models.CharField(max_length=10, choices=choose_status, default='oczekujacy')

    def __str__(self):
        return self.adres

    class Meta:
        ordering = ['date']
