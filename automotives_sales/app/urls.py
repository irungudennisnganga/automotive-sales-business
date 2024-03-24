from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('car/<int:car_id>/update/', views.update_car, name='update_car'),
    path('invoices/', views.all_invoices, name='all_invoices'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/delete/', views.delete_invoice, name='delete_invoice'), 
]