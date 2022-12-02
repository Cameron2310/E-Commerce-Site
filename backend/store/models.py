from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.URLField(max_length=300)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=200,
        unique=True
    )
    username = None

    password = models.CharField(max_length=200)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class ShoppingCart(models.Model):
    items = models.ManyToManyField(Products)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shoppingCarts')
