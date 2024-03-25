from django.db import models
from django.urls import reverse

from accounts.models import OnlineShopUser


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('shop:details-products-link', kwargs={'pk': self.pk})

class Cart(models.Model):
    user_name = models.ForeignKey(OnlineShopUser, on_delete=models.CASCADE)
    product_name = models.ManyToManyField(Products, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class CustomUser(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
