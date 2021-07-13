from django.shortcuts import render, redirect, HttpResponse
from .models import Brand, Style, Car

# Create your views here.

def brands_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brand_list.html', {'brands':brands})

def brand_detail(request, brand_id):
    return HttpResponse("New Brand WIP")

def new_brand(request):
    return HttpResponse("New Brand WIP")

def edit_brand(request, brand_id):
    return HttpResponse("Edit Brand WIP")

def car_list(request):
    return HttpResponse("Lots of Cars")

def new_car(request):
    return HttpResponse("New Car Form Here.")

def car_detail(request, car_id):
    return HttpResponse("Car Detail Page here.")

def edit_car(request, car_id):
    return HttpResponse("Edit Car Page Here")
