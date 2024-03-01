
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from shop.models import Products
from django.urls import reverse_lazy
from shop.product_form import Product_form_for_create


class ShopCreateView(CreateView):
    model =  Products
    form_class = Product_form_for_create
    success_url = reverse_lazy('home-link')
    template_name = 'product_create.html'


class ShopListView(ListView):
    model = Products
    template_name = 'product_list.html'


class ShopDetailsView(DetailView):
    model = Products
    template_name = 'product_details.html'