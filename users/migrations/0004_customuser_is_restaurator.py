# Generated by Django 4.0.4 on 2022-05-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_restaurator',
            field=models.BooleanField(default=False),
        ),
    ]
