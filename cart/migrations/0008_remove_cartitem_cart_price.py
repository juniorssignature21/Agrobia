# Generated by Django 5.0.6 on 2024-07-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_price',
        ),
    ]
