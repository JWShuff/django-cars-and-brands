from django.shortcuts import render, redirect, HttpResponse
from .forms import BrandForm, CarForm
from .models import Brand, Style, Car

# Brand Views and Functions:
def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)

def get_brand_cars(brand_id):
    return Brand.objects.all().get(cars)

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
    if request.method=="POST":
        form=BrandForm(request.POST)
        if form.is_valid():
            brand=form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else: 
        form = BrandForm()
    return render(request, 'brands/brand_form.html',{'form':form, 'type_of_request':"New"})

def edit_brand(request, brand_id):
    brand = get_brand(brand_id)
    if request.method=="POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id0)
    else:
        form=BrandForm(instance=brand)
    return render(request, 'brands/brand_form.html', {'form':form,'type_of_request':"Edit"})
# Car views and functions:

def get_car(car_id):
    return Car.objects.get(id=car_id)

def car_list(request):
    return HttpResponse("Lots of Cars")

def new_car(request):
    return HttpResponse("New Car Form Here.")

def car_detail(request, brand_id, car_id):
    return HttpResponse("Car Detail Page here.")

def edit_car(request, car_id):
    return HttpResponse("Edit Car Page Here")
