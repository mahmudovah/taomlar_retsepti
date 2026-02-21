from django.shortcuts import render
from .models import Ingredient, Meal

# Create your views here.

def index_view(request):
    meals = Meal.objects.filter(status='activ')
    print(meals)
    context = {'meals':meals}
    return render(request, 'index.html', context)

def meal_detail(request, pk):
    meal = Meal.objects.get(id=pk)
    return render(request, "meal_detail.html", context={"meal": meal})

def contact_view(request):
    return render(request, "contact.html")