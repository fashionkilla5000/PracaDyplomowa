# Generated by Django 4.0.4 on 2022-10-02 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 10, 2, 23, 57, 16, 737704))),
                ('restauracja', models.CharField(max_length=50)),
                ('czas_przygotowania', models.IntegerField(choices=[(15, '15 min'), (20, '20 min'), (30, '30 min'), (45, '45 min'), (60, '60 min')], default=15)),
                ('czas_odebrania', models.DateTimeField(blank=True, null=True)),
                ('no_of_likes', models.CharField(blank=True, max_length=50, null=True)),
                ('miasto', models.CharField(default='Olsztyn', max_length=50)),
                ('adres', models.CharField(max_length=50)),
                ('nr_mieszkania', models.CharField(blank=True, max_length=4)),
                ('płatność', models.CharField(choices=[('karta', 'Karta'), ('gotowka', 'Gotowka'), ('zaplacone', 'Zaplacone')], default='zaplacone', max_length=10)),
                ('kwota', models.CharField(max_length=5)),
                ('telefon', models.CharField(max_length=13)),
                ('komentarz', models.CharField(blank=True, max_length=200, null=True)),
                ('platforma', models.CharField(choices=[('uber', 'Uber'), ('rest', 'Rest'), ('glovo', 'Glovo'), ('tel', 'Tel')], default='glovo', max_length=5)),
                ('oczekujace', models.BooleanField(default=True)),
                ('trasa', models.BooleanField(default=False)),
                ('zakonczone', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]