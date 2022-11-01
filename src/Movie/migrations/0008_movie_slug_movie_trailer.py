# Generated by Django 4.1 on 2022-08-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0007_remove_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]