from django.shortcuts import render, HttpResponse
from .models import *
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps

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
    text = data['text'].lower()
    if text == '':
        return HttpResponse(dumps([]))
    products = Products.objects.all()
    need_products = []
    for product in products:
        if text in product.name.lower():
            need_products.append({
                'name': product.name,
                'price': product.price,
                'img': str(product.img),
                'id': product.id
            })
    return HttpResponse(dumps(need_products))

def product(request, id):
    all_products = Products.objects.filter(id=id)[0]
    return render(request, 'product.html', {'all_products': all_products})
    

            



