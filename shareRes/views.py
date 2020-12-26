from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here,
def index(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    new_restaurant = Restaurant.objects.all()
    for res in new_restaurant:
        print(res.__dict__)

    for category in categories:
        print(category.__dict__)
    restaurants = {'categories':categories,'restaurants':new_restaurant}



    print(categories.__dict__)
    return render(request, 'shareRes/index.html',restaurants)

def restaurantDetail(request,res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    data = {"restaurant":restaurant}
    return render(request, 'shareRes/restaurantDetail.html',data)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request,'shareRes/restaurantCreate.html',content)

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'categories':categories, 'restaurant':restaurant}
    return render(request, 'shareRes/restaurantUpdate.html',content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id=change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get( id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name 
    before_restaurant.restaurant_link = change_link 
    before_restaurant.restaurant_content = change_content 
    before_restaurant.restaurant_keyword == change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs = {'res_id':resId}))

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

