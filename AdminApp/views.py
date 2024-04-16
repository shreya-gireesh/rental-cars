from django.shortcuts import render, redirect
from .models import *
from UserApp.models import *
from .forms import *

# Create your views here.
def show(request):
    cars = CarModel.objects.all()
    carimg = CarImgModel.objects.all()
    carinterior = CarInteriorsModel.objects.all()
    location = LocationModel.objects.all()
    places = PlacesModel.objects.all()
    return render(request, 'admin.html', {'cars': cars, 'carimg': carimg, 'interiors': carinterior, 'location': location, 'places': places})

def car_reg(request):
    if request.method == 'POST':
        form_obj = CarModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('car_admin')
    else:
        form_obj = CarModelForm()
    return render(request, 'car_reg.html', {'form': form_obj})

def carimg_reg(request):
    if request.method == 'POST':
        form_obj = CarImgModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('car_admin')
    else:
        form_obj = CarImgModelForm()
    return render(request, 'carimg_reg.html', {'form': form_obj})

def carinterior_reg(request):
    if request.method == 'POST':
        form_obj = CarInteriorsModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('car_admin')
    else:
        form_obj = CarInteriorsModelForm()
    return render(request, 'carinterior_reg.html', {'form': form_obj})

def location_reg(request):
    if request.method == 'POST':
        form_obj = LocationModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('car_admin')
    else:
        form_obj = LocationModelForm()
    return render(request, 'location_reg.html', {'form': form_obj})

def places_reg(request):
    if request.method == 'POST':
        form_obj = PlacesModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('car_admin')
    else:
        form_obj = PlacesModelForm()
    return render(request, 'places_reg.html', {'form': form_obj})


# custom admin
def admin_home(request):
    return render(request, 'admin_home.html')

def admin_car(request):
    car = CarModel.objects.all()
    return render(request, 'admin-car.html', {'cars': car})


def admin_car_images(request):
    car = CarImgModel.objects.all()
    return render(request, 'admin-car-images.html', {'cars': car})

def admin_car_interiors(request):
    car = CarInteriorsModel.objects.all()
    return render(request, 'admin-car-interiors.html', {'cars': car})