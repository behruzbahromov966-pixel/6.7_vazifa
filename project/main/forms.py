from django import forms
from.models import Car, Brend

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    widgets = {
        'name': forms.TextInput(attrs={
            'placeholder': 'Nomi',
            'class': 'form-control'
        }),
        'manufacture_year': forms.NumberInput(attrs={
            'class': 'form-control'
        }),
        'car_owner': forms.TextInput(attrs={
            'class': 'form-control'
        }),
        'car_number': forms.TextInput(attrs={
            'class': 'form-control'
        }),
        'owner_number': forms.TextInput(attrs={
            'class': 'form-control'
        }),
        'brand': forms.Select(attrs={
            'class': 'form-control'
        }),
        'image': forms.FileInput(attrs={
            'class': 'form-control'
        })
    }
    labels = {
        "name": 'Mashina nomi',
        "manufacture_year": 'Ishlab chiqarilgan yili',
        "car_owner": "Mashina egasi",
        "car_number": "Mashina raqami",
        "owner_number": "Mashina egasining tel.raqami",
        "brand": "Mashina brandi",
        "image": "Mashina rasmi"
    }