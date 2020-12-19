from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here,
def index(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    print(categories.__dict__)
    return render(request, 'shareRes/index.html',content)

def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    return render(request,'shareRes/restaurantCreate.html')

def categoryCreate(request):
    return render(request,'shareRes/categoryCreate.html')

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

