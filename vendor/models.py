from django.db import models
from django.contrib.auth.models import User
from categories.models import ProductCategory


class Farmers(models.Model):
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    farm_produce = models.CharField(max_length=255)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farmers', default=1)
    
    def __str__(self):
        return self.company_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/product/', default='')
    stock = models.IntegerField()
    productcategories = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE, default='')
    vendor = models.ForeignKey(Farmers, related_name='farmers', on_delete=models.CASCADE, default='')
    created = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
