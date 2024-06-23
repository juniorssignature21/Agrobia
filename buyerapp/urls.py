from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.products_page, name='shop'),
    path('product/<int:pk>', views.single_product, name='product'),
    path('product/<int:pk>', views.single_product, name='product'),
]

