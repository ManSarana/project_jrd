from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def foods(request):
    return HttpResponse('เมนูอร่อย ส่งบ่อย ส่งแม่น')

def food(request, food_id):
    return HttpResponse('this menu ID = ' + str(food_id))