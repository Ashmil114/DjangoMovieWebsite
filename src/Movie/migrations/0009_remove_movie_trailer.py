# Generated by Django 4.1 on 2022-08-28 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0008_movie_slug_movie_trailer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailer',
        ),
    ]