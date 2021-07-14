from django.shortcuts import render, redirect, HttpResponse
from .models import Brand, Style, Car


def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)

def brands_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brand_list.html', {'brands':brands})

def brand_detail(request, brand_id):
    brand = get_brand(brand_id)
    return render(request, 'brands/brand_detail.html', {'brand':brand})

def delete_brand(request, brand_id):
    if request.method=='POST':
        brand=get_brand(brand_id)
        brand.delete()
    return redirect('brand_list')

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
