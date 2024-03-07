from django.db import models
from accounts.models import OnlineShopUser

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')



class Cart(models.Model):
    user_name = models.ForeignKey(OnlineShopUser, on_delete=models.CASCADE)
    product_name = models.ManyToManyField(Products)

