from category.models import Category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product 
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    products = Product.objects.all()
    category = Category.objects.all() 
    context = {'products': products, 'ctg': category}
    return render(request, 'home.html', context)


def index(request):
    return render(request, 'index.html')

def category(request):
    category = Category.objects.all() 
    return  render(request, 'home.html')

def home(request):
    return render(request, 'home.html')