from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def home(request):
    categories = Category.objects
    products = Product.objects
    return render(request, 'home.html', {'categories': categories, 'products': products})


def product(request):
    categories = Category.objects
    return render(request, 'product.html', {'categories': categories})