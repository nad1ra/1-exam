
from django.db import models

class Meal(models.Model):
    TYPE_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('main course', 'Main Course'),
        ('desert', 'Desert')
    ]
    meal_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=20)
    type = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)



