from django.contrib import admin
from .models import UserProfile, Car, Invoice, Customer, Sale
# Register your models here.

# admin.site.register(UserProfile)
admin.site.register(Car)
admin.site.register(Invoice)
admin.site.register(Customer)
admin.site.register(Sale)