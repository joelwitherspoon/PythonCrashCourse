from django.db import models

# Create your models here.

class Pizza(models.Model):
    """The pizza the customer is ordering"""
    """Python 18-4 Pizzas"""
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        """Return name"""
        return self.name
    
class Topping(models.Model):
    """The pizza toppings the customer is ordering"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
        

    