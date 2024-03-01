from django.urls import path
from shop.views import ShopCreateView
from shop.views import ShopListView
from shop.views import ShopDetailsView


urlpatterns = [
    path('create/', ShopCreateView.as_view(), name="create-product-link"),
    path('list/', ShopListView.as_view(), name="list-products-link"),
    path('details/<int:pk>', ShopDetailsView.as_view(), name="details-products-link"),
]
