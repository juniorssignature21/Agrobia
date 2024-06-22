from django.shortcuts import render, redirect
from .forms import SignUpForm, UserImg
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from vendor.models import Product
from categories.models import ProductCategory

# def home(request):
#     return render(request, 'store/home.html')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("you have registered successfully!!!"))
            return redirect("home")
        else:
            messages.success(request, ("there was a problem registering!!!"))
            return redirect("register")
    else:
        return render(request, 'store/register.html', {"form": form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Logged in successfully!!!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error please try again!!!"))
            return redirect('home')
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out!!!"))
    return redirect('home')

def product_section(request):
    product = Product.objects.all()[:6]
    categories = ProductCategory.objects.all()
    context = {'product': product, 'categories': categories}
    return render(request, 'store/home.html', context)

def user_img(request):
    form = UserImg()
    if request.method == 'POST':
        form = UserImg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'store/image-upload.html', context)
    
