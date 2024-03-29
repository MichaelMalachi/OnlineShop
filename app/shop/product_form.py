from django import forms
from shop.models import Products
from .models_choices import BRAND_TYPES

class Product_form_for_create(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            'name',
            'description',
            'car_brand',
            'price',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super(Product_form_for_create, self).__init__(*args, **kwargs)
        self.fields['car_brand'].widget = forms.Select(choices=BRAND_TYPES)
