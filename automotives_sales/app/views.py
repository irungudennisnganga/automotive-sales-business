from django.shortcuts import render, redirect
from .models import Car,Invoice
from .serializer import InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarUpdateForm,InvoiceForm
from rest_framework.decorators import api_view

def home(request):
    return render(request, 'home.html') 

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

def delete_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a success response without content
    return Response(status=status.HTTP_400_BAD_REQUEST) 