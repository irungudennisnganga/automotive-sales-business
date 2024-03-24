# import os
# import django
# from django.conf import settings
# from django.contrib.auth.models import User
# from models import UserProfile, Car, Sale, Customer, Invoice
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automotives_sales.settings')
# django.setup()



# def seed():
#     # Create users
#     admin_user = User.objects.create(username='admin', email='admin@example.com', password='adminpassword')
#     seller_user = User.objects.create(username='seller', email='seller@example.com', password='sellerpassword')

#     # Create user profiles
#     admin_profile = UserProfile.objects.create(user=admin_user, role='admin')
#     seller_profile = UserProfile.objects.create(user=seller_user, role='seller')

#     # Create customers
#     customer1 = User.objects.create(username='customer1', email='customer1@example.com', password='customer1password')
#     customer2 = User.objects.create(username='customer2', email='customer2@example.com', password='customer2password')

#     customer1_profile = Customer.objects.create(user=customer1, address='123 Main St', phone_number='1234567890')
#     customer2_profile = Customer.objects.create(user=customer2, address='456 Elm St', phone_number='9876543210')

#     # Create cars
    # car1 = Car.objects.create(
    #     make='Toyota', model='Camry', year=2022, vin='12345678901234567',
    #     mileage=10000, color='Red', body_style='Sedan', transmission='Automatic',
    #     fuel_type='Gasoline', engine_size='2.5L', drive_type='Front-wheel drive', trim_level='LE'
    # )
    # car2 = Car.objects.create(
    #     make='Honda', model='Civic', year=2021, vin='23456789012345678',
    #     mileage=8000, color='Blue', body_style='Sedan', transmission='Manual',
    #     fuel_type='Gasoline', engine_size='2.0L', drive_type='Front-wheel drive', trim_level='Sport'
    # )

#     # Create sales
#     sale1 = Sale.objects.create(
#         car=car1, seller=admin_profile, customer=customer1_profile,
#         sale_status='Sealed', sale_date='2023-01-15'
#     )
#     sale2 = Sale.objects.create(
#         car=car2, seller=seller_profile, customer=customer2_profile,
#         sale_status='Quoted', sale_date='2023-02-20'
#     )

#     # Create invoices
#     invoice1 = Invoice.objects.create(
#         sale=sale1, receipt_number='INV-001', date_of_purchase='2023-01-15',
#         seller_info='Admin', buyer_info='Customer 1', vehicle_info=car1,
#         payment_method='Cash', amount_paid=25000.00
#     )
#     invoice2 = Invoice.objects.create(
#         sale=sale2, receipt_number='INV-002', date_of_purchase='2023-02-20',
#         seller_info='Seller', buyer_info='Customer 2', vehicle_info=car2,
#         payment_method='Credit Card', amount_paid=30000.00
#     )

# if __name__ == '__main__':
#     seed()


