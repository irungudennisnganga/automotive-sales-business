from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
     path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
      path('car/<int:car_id>/update/', views.update_car, name='update_car'),
]
