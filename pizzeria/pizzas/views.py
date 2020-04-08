from django.shortcuts import render

from .models import Pizza
# Create your views here.

def index(request):
    """The home for pizzas"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Display pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    """Display a pizza and toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-id')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request,'pizzas/toppings.html',context)
    
