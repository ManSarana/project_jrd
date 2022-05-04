from datetime import datetime
from django.shortcuts import render

# Create your views here.

all_foods = [
    {'id' : 1, 'title' : 'Dark choco premium'
    , 'price' : 2499, 'is_premium' : True
    , 'promotion_end_at' : datetime(2022, 2, 28)},
    {'id' : 2, 'title' : 'Red Spicy'
    , 'price' : 349, 'is_premium' : False
    , 'promotion_end_at' : datetime(2022, 2, 15)},
    {'id' : 3, 'title' : 'Blue Glacier'
    , 'price' : 349, 'is_premium' : False
    , 'promotion_end_at' : datetime(2022, 2, 15)},
]

def foods(request):
    context = {'foods' : all_foods}
    return render(request, 'app_food/foods.html', context)

def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError:
        print('Index Error')
    context = {'food' : one_food}
    return render(request,
     'app_food/food.html', context)