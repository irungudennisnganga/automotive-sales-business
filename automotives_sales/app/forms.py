# forms.py
from django import forms
from .models import Car,Invoice

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # You can customize this to include specific fields you want to update
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'  # You can also specify specific fields if neede