# vendorapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, VendorForm
from vendor.models import Product, Farmers

@login_required(login_url='login')
def vendorform(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-upload')
    else:
        form = VendorForm()
    context = {'form': form}
    return render(request, 'vendorapp/vendorform.html', context)
 
@login_required(login_url='login')
def productsupload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            try:
                farmer = Farmers.objects.get(farmer=request.user)
                product.vendor = farmer
                product.save()
                return redirect('products-pages')
            except Farmers.DoesNotExist:
                # Handle the case where the farmer does not exist
                return redirect('vendor-form')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'vendorapp/index.html', context)

@login_required(login_url='login')
def product_pages(request):
    try:
        farmer = Farmers.objects.get(farmer=request.user)
        products = Product.objects.filter(vendor=farmer)
    except Farmers.DoesNotExist:
        # Handle the case where the farmer does not exist
        products = []
    return render(request, 'vendorapp/products_page.html', {'products': products})
