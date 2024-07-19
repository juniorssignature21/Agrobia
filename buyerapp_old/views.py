from buyer.models import Order, Product
from cart.models import Cart, CartItem
from vendor.models import Farmers
from categories.models import ProductCategory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q


def products_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    products = Product.objects.filter(
        Q(name__icontains=q)
        )
    farmer = Farmers.objects.all()
    # products = Product.objects.all()
    context = {'products': products, 'farmer': farmer}
    return render(request, 'buyerapp/products.html', context)

def single_product(request, pk):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    product = Product.objects.get(id=pk)
    context = {
            'cart': cart,
            'cart_items': cart_items,
            'product': product,
        }
    return render(request, 'buyerapp/single_product.html', context)
