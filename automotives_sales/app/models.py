from django.db import models
from django.contrib.auth.models import User

# User Management Module
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


# Inventory Management Module
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
    mileage = models.IntegerField()
    color = models.CharField(max_length=50)
    body_style = models.CharField(max_length=50)
    transmission = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    engine_size = models.CharField(max_length=20)
    drive_type = models.CharField(max_length=20)
    trim_level = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    # country_of_origin = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    # import_document = models.OneToOneField('ImportDocument', on_delete=models.SET_NULL, null=True)
    # Add gallery - consider using a separate model for images
  
    
# Sales Tracking Module
class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    sale_status_choices = (
        ('Inquired', 'Inquired'),
        ('Quoted', 'Quoted'),
        ('Sealed', 'Sealed'),
    )
    sale_status = models.CharField(max_length=20, choices=sale_status_choices)
    sale_date = models.DateField()    
    
# Customer Module
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    
    
# Billing System Module
class Invoice(models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=50)
    date_of_purchase = models.DateField()
    seller_info = models.CharField(max_length=255)
    buyer_info = models.CharField(max_length=255)
    vehicle_info = models.ForeignKey(Car, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
   
        