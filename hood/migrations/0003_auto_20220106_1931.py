# Generated by Django 3.2.7 on 2022-01-06 16:31

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20211224_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='hood_image'),
        ),
    ]
