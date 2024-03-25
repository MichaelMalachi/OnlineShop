from django.db.models import Q
from django.shortcuts import render
from shop.models import Products

def search_products(request):
    query = request.GET.get('q', None)
    products = []
    if query:
        search_terms = query.split()
        filter_condition = Q()
        for term in search_terms:
            filter_condition |= Q(name__icontains=term)
        products = Products.objects.filter(filter_condition)[:10]
        print("*"*100)
        print(products)
        print("*"*100)
    return render(request, 'search_results.html', {'products': products})
