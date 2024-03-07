from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from shop.models import Products
from django.urls import reverse_lazy, reverse
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


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Products
from django.shortcuts import redirect, get_object_or_404

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    # Предполагается, что у вас есть аутентификация пользователей и вы можете получить текущего пользователя
    user = request.user
    # Получаем или создаем корзину для текущего пользователя
    cart, created = Cart.objects.get_or_create(user_name=user)
    # Добавляем выбранный товар в корзину
    cart.product_name.add(product)
    # После добавления товара в корзину, вы можете выполнить редирект на страницу корзины или на страницу, с которой был выполнен запрос
    return redirect('home-link')

@login_required
def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user_name=user)
    products = cart.product_name.all()  # Используйте product_name, а не products
    total_price = sum(product.price for product in products)
    return render(request, 'cart.html', {'cart_items': products, 'total_price': total_price})


