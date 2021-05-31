from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return render(request,'shop/index.html')
def about(request):
    return render(request,'shop/about.html')
def basic(request):
    return render(request, "shop/basic.html")
def productview(request):
    return HttpResponse("we are prpductview")
def track(request):
    return HttpResponse("we are track")