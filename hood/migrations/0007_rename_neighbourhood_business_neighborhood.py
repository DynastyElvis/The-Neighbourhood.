# Generated by Django 3.2.7 on 2022-01-10 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood',
            new_name='neighborhood',
        ),
    ]
