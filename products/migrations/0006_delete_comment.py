# Generated by Django 3.0.1 on 2021-01-20 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
