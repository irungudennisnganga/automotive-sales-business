from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/create', views.create_car, name='create_car'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('car/<int:car_id>/update/', views.update_car, name='update_car'),
    path('invoices/', views.all_invoices, name='all_invoices'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:invoice_id>/delete/', views.delete_invoice, name='delete_invoice'), 
]