from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CarUpdateForm, InvoiceForm, SignUpForm, CarCreateForm
from .models import Car, Invoice
from .serializer import InvoiceSerializer
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Refresh the form to get the latest user instance
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def custom_logout(request):
    logout(request)
    return redirect('login')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'car_list': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('car_list')

def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarUpdateForm(request.POST,request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = CarUpdateForm(instance=car)

    return render(request, 'update_car.html', {'form': form, 'car': car})

def create_car(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('car_list')  # Redirect to the list of cars after successful creation
    else:
        form = CarCreateForm()
        pass
    return render(request, 'create_car.html', {'form': form})

def all_invoices(request):
    
    invoices = Invoice.objects.all()
    return render(request, 'invoice.html', {'invoices': invoices})

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice_details.html', {'invoice': invoice})

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')  # Redirect to the list of invoices
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})

def update_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('invoice_list')
    else:
        serializer = InvoiceSerializer(instance=invoice)
    return render(request, 'update_invoice.html', {'form': serializer})


def delete_invoice(request, invoice_id):
   
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.delete()
    return redirect('all_invoices')
  