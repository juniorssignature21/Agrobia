from buyer.models import Order, Product
from vendor.models import Farmers
from django.shortcuts import render, redirect


def products_page(request):
    farmer = Farmers.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'farmer': farmer}
    return render(request, 'buyerapp/products.html', context)

def single_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'buyerapp/single_product.html', context)