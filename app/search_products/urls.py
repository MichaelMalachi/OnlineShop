from django.urls import path
from .views import search_products
from .views import autocomplete

app_name = 'search_products'

urlpatterns = [
    path('search', search_products, name='search'),
path('autocomplete', autocomplete, name='autocomplete'),
]