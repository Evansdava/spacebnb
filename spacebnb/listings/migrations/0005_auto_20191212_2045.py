# Generated by Django 3.0 on 2019-12-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20191212_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='img_url',
            field=models.URLField(default='https://via.placeholder.com/300'),
        ),
    ]
