from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'category', 'image', 'cost']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ProductsSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ['items', 'user']
