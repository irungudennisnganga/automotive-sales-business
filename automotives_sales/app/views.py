from django.shortcuts import render
from .models import Car
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarUpdateForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'car_list': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('car_list')

# views.py

def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarUpdateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = CarUpdateForm(instance=car)

    return render(request, 'update_car.html', {'form': form, 'car': car})
