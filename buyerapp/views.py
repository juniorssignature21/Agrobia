from buyer.models import Order, Product
from django.shortcuts import render, redirect


def products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'buyerapp/products.html', context)