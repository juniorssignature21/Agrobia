# Generated by Django 5.0.6 on 2024-06-19 20:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_product_vendor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmers',
            name='farmer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='farmers', to=settings.AUTH_USER_MODEL),
        ),
    ]
