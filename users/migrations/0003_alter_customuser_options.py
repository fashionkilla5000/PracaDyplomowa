# Generated by Django 4.0.4 on 2022-05-27 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_driver'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['date_joined']},
        ),
    ]
