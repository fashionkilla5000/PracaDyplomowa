# Generated by Django 4.0.4 on 2022-08-27 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_rename_comment_post_komentarz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='payment',
            new_name='płatność',
        ),
    ]
