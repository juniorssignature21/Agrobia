from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendorform, name='vendor-form'),
    path('product_upload/', views.productsupload, name='products-upload'),
    path('product_page/', views.product_pages, name='products-pages'),
]
