from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.ProductsAPIView.as_view()),
    path('cart/', views.ShoppingCartAPIView.as_view()),
    path('shopping-cart/', views.index),
    path('<str:category>/', views.index),
    path('<str:category>/<int:id>/', views.index),
    path('login/', views.UserAPIView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
