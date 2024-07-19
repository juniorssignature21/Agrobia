from django.db import models
from django.contrib.auth.models import User
from vendor.models import Product, ProductCategory


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    user_img = models.ImageField(default='', upload_to='uploads/product/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='orders', default='')
    buyer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
    
