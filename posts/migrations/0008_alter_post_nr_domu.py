# Generated by Django 4.0.4 on 2022-08-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_nr_domu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nr_domu',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
