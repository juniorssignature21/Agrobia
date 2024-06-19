from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.products_page, name='shop'),
]

