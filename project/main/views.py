from django.shortcuts import render
from django.http import HttpResponse

from .models import Brend, Car
# Create your views here.

def index(request):
    brands = Brend.objects.all()
    cars = Brend.objects.all()

    context = {
        "brands": brands,
        "cars": cars,
        "title": "FanCars"
    }

    return render(request, 'main/index.html', context)

def detail(request, car_id):
    car = Car.objects.get(id=car_id)

    context = {
        "car": car,
        "title": car.name
    }

    return render(request, 'main/detail.html', context)

def car_by_brand(request, brand_id):
    brands = Brend.objects.all()
    brand = Brend.objects.get(id=brand_id)
    cars = Car.objects.filter(brand=brand)

    context = {
        "brands": brands,
        "cars": cars,
        "title": "FanCars"
    }

    return render(request, 'main/index.html', context)