from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    restaurants = Shop_info.objects.filter()
    return render(request, 'home.html', {'restaurants': restaurants})

@require_http_methods(["POST"])
def search(request):
    return HttpResponse(request.POST)

@require_http_methods(["POST"])
@csrf_exempt
def search_mini(request):
    data = loads(request.body)
    text = data['text']
    if text == '':
        return HttpResponse(dumps([]))
    products = Products.objects.filter(name__contains=text)
    print(products)
    need_products = []
    for product in products:
        need_products.append({
            'name': product.name,
            'price': product.price,
            'img': str(product.img),
            'id': product.id,
            'description': str(product.description),
            'shop': str(product.shop)
        })
    return HttpResponse(dumps(need_products))

def product(request, id):
    all_products = Products.objects.filter(id=id)[0]
    return render(request, 'product.html', {'all_products': all_products})

def start_login(request):
    data = request.POST
    login_ = data['nickname']
    password = data['password']
    user = authenticate(request, username=login_, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
         return HttpResponse('false')
    
def profile_logout(request):
    logout(request)
    return redirect('/')




    

            



