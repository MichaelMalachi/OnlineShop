from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from shop.product_form import Product_form_for_create
from django.http import HttpResponseBadRequest
from .models import Cart, Products
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from shop.models import CartItem


class ShopCreateView(CreateView):
    model = Products
    form_class = Product_form_for_create
    success_url = reverse_lazy('home-link')
    template_name = 'product_create.html'


class ShopListView(ListView):
    model = Products
    template_name = 'product_list.html'


class ShopDetailsView(DetailView):
    model = Products
    template_name = 'product_details.html'


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Получаем идентификатор продукта из формы
        quantity = request.POST.get('quantity')  # Получаем количество товара из формы

        if product_id and quantity:
            product = get_object_or_404(Products, pk=product_id)
            user = request.user
            cart, created = Cart.objects.get_or_create(user_name=user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity = int(quantity)  # Увеличиваем количество товара, если он уже есть в корзине
            cart_item.save()
            return redirect('home-link')
        else:
            return HttpResponseBadRequest("Product ID and quantity are required.")
    else:
        return HttpResponseBadRequest("Only POST method is allowed.")


def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user_name=request.user if request.user.is_authenticated else None)
    total_price = 0
    total_quantity = 0
    for item in cart_items:
        total_price += item.quantity * item.product.price
        total_quantity += item.quantity
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity
    }
    return render(request, 'cart.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('shop:cart')
