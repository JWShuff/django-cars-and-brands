from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name')

class BrandForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name', 'style','brand')