from django.contrib import admin
from django.contrib.admin import ModelAdmin
from shop.models import Products
from accounts.models import OnlineShopUser


class ProductsAdmin(ModelAdmin):
    resource_class = Products
    list_display = (
        'name',
        'description',
        'car_brand',
        'price',
        'image',
    )
    list_filter = (
        'name',
        'description',
        'car_brand',
        'price',

    )
    search_fields = (
        'name',
        'description',
        'car_brand',
        'price',
    )

    # readonly_fields = (
    #     "sale",
    #     "buy",
    # )

    # def has_delete_permission(self, request, obj=None):
    #     return True


admin.site.register(Products, ProductsAdmin)



class OnlineShopUserAdmin(ModelAdmin):
    resource_class = OnlineShopUser
    list_display = (
        'email',
        'is_superuser',
        'last_login',
        'is_staff',
        'is_active',
        'date_joined',


    )
    list_filter = (
        'last_login',
        'is_superuser',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'email',


    )
    search_fields = (
        'last_login',
        'is_superuser',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'email',

    )

    readonly_fields = (
        'last_login',
        'is_superuser',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'email',

    )

    # def has_delete_permission(self, request, obj=None):
    #     return True


admin.site.register(OnlineShopUser, OnlineShopUserAdmin)