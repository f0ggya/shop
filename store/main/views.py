from django.shortcuts import render, HttpResponse
from .models import *
from django.views.decorators.http import require_http_methods

def home(request):
    restaurants = Shop_info.objects.filter()
    return render(request, 'home.html', {'restaurants': restaurants})

@require_http_methods(["POST"])
def search(request):
    return HttpResponse(request.POST)



