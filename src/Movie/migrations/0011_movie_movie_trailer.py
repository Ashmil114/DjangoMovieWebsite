# Generated by Django 4.1 on 2022-08-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0010_remove_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]