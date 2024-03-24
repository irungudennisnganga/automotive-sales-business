# forms.py
from django import forms
from .models import Car,Invoice
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # You can customize this to include specific fields you want to update
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'  # You can also specify specific fields if neede