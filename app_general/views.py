from django.shortcuts import render
from django.shortcuts import  HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')
