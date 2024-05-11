from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm


def cars_view(request):
    cars = Car.objects.all().order_by('model') #mostra todos
    #cars = Car.objects.filter(brand__name= 'FIAT') #filtrando brand com nome FIAT case sensitive
    #cars = Car.objects.filter(brand=1) #filtrando pelo id da tabela
    #cars = Car.objects.filter(model__contains='x') #filtrando por x que contenha no nome, não é case sensitive

    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search)

    return render(request, 'cars.html', {'cars': cars})


def new_car_view(request):
    new_car_form = CarForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})

