from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def shopping_cart(request):    
    return render(request, 'cart/shopping_cart.html')