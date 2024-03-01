from django import forms
from shop.models import Products

class Product_form_for_create(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            'name',
            'description',
            'price',
            'image',
        )