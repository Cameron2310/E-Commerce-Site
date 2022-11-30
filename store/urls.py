from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shopping-cart/', views.cart, name='shopping_cart'),
    path('shopping-cart/<int:product_id>/update/',
         views.update_cart, name='update_cart'),
    path('search/', views.search, name='search_results'),
    path('<str:category>/', views.category, name='categories'),
    path('<str:category>/<int:product_id>/', views.product, name='products'),
    path('<str:category>/<int:product_id>/add_to_cart/',
         views.add_to_cart, name='cart_add'),
]

urlpatterns += staticfiles_urlpatterns()
