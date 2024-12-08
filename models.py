from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone

class PetFood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name="pet_foods", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_food_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_food = models.ForeignKey(PetFood, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.pet_food.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order by {self.user.username} on {self.ordered_at}"

from django.db import models


