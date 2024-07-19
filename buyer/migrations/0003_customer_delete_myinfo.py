# Generated by Django 5.0.6 on 2024-07-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user_img', models.ImageField(default='', upload_to='uploads/product/')),
            ],
        ),
        migrations.DeleteModel(
            name='MyInfo',
        ),
    ]