# Generated by Django 5.0.6 on 2024-07-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_temporar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='temporar',
        ),
    ]