from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def foods(request):
    return render(request, 'app_food/foods.html')

def food(request, food_id):
    return render(request, 'app_food/food.html', context={'food_id': food_id})