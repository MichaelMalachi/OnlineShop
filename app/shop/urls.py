from django.urls import path
from shop.views import ShopCreateView
from shop.views import ShopListView
from shop.views import ShopDetailsView
from shop.views import add_to_cart
from shop.views import add_to_cart_AnonymousUser
from shop.views import view_cart
from shop.views import ProductDeleteView
from shop.views import view_cart_AnonymousUser
from shop.views import remove_from_cart_AnonymousUser


from shop.views import remove_from_cart

app_name = 'shop'

urlpatterns = [
    path('create/', ShopCreateView.as_view(), name="create-product-link"),
    path('list/', ShopListView.as_view(), name="list-products-link"),
    path('details/<int:pk>', ShopDetailsView.as_view(), name="details-products-link"),
    path('cart/', view_cart, name='cart'),
    path('cart_Anonymous_User/', view_cart_AnonymousUser, name='cart_AnonymousUser'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('add_to_cart_Anonymous_User/', add_to_cart_AnonymousUser, name='add_to_cart_AnonymousUser'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove_from_cart_AnonymousUser/<int:cart_item_id>/', remove_from_cart_AnonymousUser,
         name='remove_from_cart_AnonymousUser'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
    ]
