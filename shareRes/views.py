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
    categories = Category.objects.all()
    content = {'categories':categories}
    

    return render(request,'shareRes/restaurantCreate.html',content)

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    for val in content['categories']:
        print(val.__dict__)    
        
    return render(request,'shareRes/categoryCreate.html',content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

def Create_restaurant(request):
    resCategory = request.POST['resCategory']
    resTitle = request.POST['resTitle']
    resLink = request.POST['resLink']
    resContent = request.POST['resContent']
    resLoc = request.POST['resLoc']
    new_restaurant = Restaurant(category_id = resCategory,restaurant_name =resTitle ,restaurant_link =resLink ,restaurant_content = resContent, restaurant_keyword =resLoc )
    new_restaurant.save()
    return HttpResponseRedirect(reverse('index'))
