# Generated by Django 5.0.6 on 2024-06-19 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_farmers_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default='auth-user', on_delete=django.db.models.deletion.CASCADE, related_name='farmers', to='vendor.farmers'),
        ),
    ]