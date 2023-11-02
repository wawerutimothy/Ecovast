from django.shortcuts import render
from item.models import Category, Item

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:20] # to get 1-20
    categories = Category.objects.all() # to get all categories
    return render(request, 'core/index.html', {
        'categories':categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')