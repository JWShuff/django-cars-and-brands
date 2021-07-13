# 

# 

from django.urls import path
from . import views


urlpatterns = [
    # /brands  # a list of all the car brands
    path('', views.brands_list, name='brand_list'),
    # /brands / new  # form for a new car brand
    path('new/', views.new_brand, name='new_brand'),
    # /brands / <: id >  # see a specific car brand
    path('<int:brand_id>/', views.brand_detail, name='brand_detail'),
    # /brands / <: id > /edit  # edit page for a specific car brand
    path('<int:brand_id>/edit', views.edit_brand, name='edit_brand'),
    # /brands / <: brand_id > /cars  # a list of cars for a specific car brand
    path('<int:brand_id>/cars', views.car_list, name='car_list'),
    # /brands / <: brand_id > /cars / new  # form for a new car under a specific car brand
    path('<int:brand_id>/cars/new/', views.new_car, name='new_car'),
    # /brands / <: brand_id > /cars / <: car_id >  # see a specific car for a specific car brand
    path('<int:brand_id>/cars/<int:car_id>/', views.car_detail, name='car_detail'),
    # /brands / <: brand_id > /cars / <: car_id > /edit  # edit page for a specific car under a specific car brand
    path('<int:brand_id/cars/<int:car_id>/edit', views.edit_car, name='edit_car'),
]
