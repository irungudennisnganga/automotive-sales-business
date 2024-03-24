# forms.py
from django import forms
from .models import Car

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # You can customize this to include specific fields you want to update
