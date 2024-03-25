from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from shop.product_form import Product_form_for_create
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Cart, CartItem, Products


class ShopCreateView(CreateView):
    model = Products
    form_class = Product_form_for_create
    success_url = reverse_lazy('home-link')
    template_name = 'product_create.html'


class ShopListView(ListView):
    model = Products
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_brands'] = Products.objects.values_list('car_brand', flat=True).distinct()
        return context


class ShopDetailsView(DetailView):
    model = Products
    template_name = 'product_details.html'

class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('shop:list-products-link')
    template_name = 'products_confirm_delete.html'
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


def add_to_cart_AnonymousUser(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        if product_id and quantity:
            product = get_object_or_404(Products, pk=product_id)
            if 'cart' not in request.session:
                request.session['cart'] = {}
            cart = request.session['cart']
            if product_id in cart:
                cart[product_id] += int(quantity)
            else:
                cart[product_id] = int(quantity)
            request.session.modified = True
            return redirect('home-link')
        else:
            return HttpResponseBadRequest("Product ID and quantity are required.")
    else:
        return HttpResponseBadRequest("Only POST method is allowed.")


@login_required
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


def view_cart_AnonymousUser(request):
    if 'cart' in request.session:
        cart_items = []
        total_price = 0
        total_quantity = 0

        for product_id, quantity in request.session['cart'].items():
            product = get_object_or_404(Products, pk=product_id)
            total_price += product.price * quantity
            total_quantity += quantity
            cart_items.append({'product': product, 'quantity': quantity})

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'total_quantity': total_quantity
        }
    else:
        context = {'cart_items': [], 'total_price': 0, 'total_quantity': 0}

    return render(request, 'cart.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('shop:cart')


def remove_from_cart_AnonymousUser(request, cart_item_id):
    if 'cart' in request.session:
        cart = request.session['cart']
        if str(cart_item_id) in cart:
            del cart[str(cart_item_id)]
            request.session.modified = True
    return redirect('shop:cart_AnonymousUser')


