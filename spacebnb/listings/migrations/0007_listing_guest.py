# Generated by Django 3.0 on 2019-12-13 22:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0006_listing_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='guest',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
