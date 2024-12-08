from rest_framework import serializers
from .models import PetFood, Order

# PetFood serializer
class PetFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetFood
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'pet_food', 'quantity', 'total_price', 'ordered_at']
