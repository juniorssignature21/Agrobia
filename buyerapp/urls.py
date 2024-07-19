from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.products_page, name='shop'),
    path('product/<int:pk>', views.single_product, name='product'),
    path('category-summary/', views.category_summary, name='category-summary'),
    path('category/<str:foo>', views.category, name='category'),

    # path('categories/<str:foo>', views.category, name='categories'),
]

