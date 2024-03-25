from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car, Invoice

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    password1 =forms.CharField()
    password2 =forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'vin', 'mileage', 'color', 'body_style', 'transmission', 'fuel_type', 'engine_size', 'drive_type', 'trim_level', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the 'multipart/form-data' attribute to the form for handling file uploads
        self.fields['image'].widget.attrs['enctype'] = 'multipart/form-data'