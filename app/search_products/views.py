from django.db.models import Q
from django.shortcuts import render
from shop.models import Products
from django.http import JsonResponse


def search_products(request):
    query = request.GET.get('q', None)
    products = []
    if query:
        search_terms = query.split()
        filter_condition = Q()
        for term in search_terms:
            filter_condition |= Q(name__icontains=term)
        products = Products.objects.filter(filter_condition)[:10]
    return render(request, 'search_results.html', {'products': products})


def autocomplete(request):
    term = request.GET.get('term', None)
    products = []
    if term:
        products = list(Products.objects.filter(name__icontains=term).values_list('name', flat=True))
    return JsonResponse(products, safe=False)
