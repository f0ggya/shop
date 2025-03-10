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

def start_reg(request):
    data = request.POST
    login_ = data['nickname']
    password = data['password1']
    user = authenticate(request, username=login_, password=password)
    if user is not None:
        return HttpResponse('false')
    User.objects.create_user(login_, '', password)
    user = authenticate(request, username=login_, password=password)
    Cart.objects.create(owner=user, cart_products=[])
    login(request, user)
    return redirect('/')

def profile(request):
    user = User.objects.get(id = request.user.id)
    shops = Shop_info.objects.filter(owner=user)
    return render(request, 'profile.html', {'shops': shops})

@require_http_methods(["POST"])
@csrf_exempt
def change_profile(request):
    data = loads(request.body)
    login_ = data['login']
    password1 = data['password1']
    password2 = data['password2']
    user = User.objects.get(id = request.user.id)
    user.set_password(password1)
    user.username = login_
    user.save()
    return redirect('/')

@require_http_methods(["POST"])
@csrf_exempt
def create_shop(request):
    user = User.objects.get(id = request.user.id)
    shop = Shop_info.objects.create(owner=user)
    js_shop = dumps({'name': shop.name, 'bg': shop.background_color, 'url': shop.url})
    return HttpResponse(js_shop)

def update(request, id):
    data = request.POST
    name = data['name']
    color = data['color']
    url = data['url']
    file_name = data['file']
    Shop_info.objects.filter(id=id).update(name=name, background_color=color, url=url, img=file_name)
    return redirect('/')

def add_products(request, id):
    shop = Shop_info.objects.get(id=id)
    products = Products.objects.filter(shop=shop)
    return render(request, 'add_product.html', {'products': products, 'shop': shop})
    
def add_product(request, id):
    data = request.POST
    name = data['name']
    img = data['img']
    description  = data['description']
    price = data['price']
    shop = Shop_info.objects.get(id=id)
    products = Products.objects.filter(shop=shop)
    Products.objects.create(name=name, img=img, description=description, price=price, shop=shop)
    return render(request, 'add_product.html', {'products': products, 'shop': shop})

@require_http_methods(["DELETE"])
@csrf_exempt
def del_product(request):
    data = loads(request.body)
    Products.objects.filter(id=data['id']).delete()
    return HttpResponse(200)

def update_product(request, id):
    data = request.POST
    name = data['name']
    img = data['img']
    description = data['description']
    price = data['price']
    product = Products.objects.get(id=id)
    product.name = name
    product.img = img
    product.description = description
    product.price = price
    product.save()
    products = Products.objects.filter(shop=product.shop)
    return render(request, 'add_product.html', {'products': products, 'shop': product.shop})

def catalog(request, id):
    shop = Shop_info.objects.get(id=id)
    products = Products.objects.filter(shop=shop)
    return render(request, 'catalog.html', {'shop':shop, 'products': products})

def cart(request):
    cart = Cart.objects.get(owner=request.user)
    return render(request, 'cart.html', {'products':cart.cart_products['cart']})

@require_http_methods(["POST"])
@csrf_exempt            
def add_cart(request):
    data = loads(request.body)
    id = data['id']
    product = Products.objects.get(id=id)
    product_json = {
        'name': product.name,
        'img': str(product.img),
        'price': product.price      
    }
    cart = Cart.objects.get(owner=request.user)
    cart.cart_products["cart"][product.id] = product_json
    cart.save()
    return HttpResponse(200)
