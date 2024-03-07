from django.urls import path
from shop.views import ShopCreateView
from shop.views import ShopListView
from shop.views import ShopDetailsView
from shop.views import add_to_cart
from shop.views import view_cart

app_name = 'shop'
urlpatterns = [
    path('create/', ShopCreateView.as_view(), name="create-product-link"),
    path('list/', ShopListView.as_view(), name="list-products-link"),
    path('details/<int:pk>', ShopDetailsView.as_view(), name="details-products-link"),
    path('cart/', view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

]
