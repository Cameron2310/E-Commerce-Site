from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.ProductsAPIView.as_view(), name='home'),
    path('cart/', views.ShoppingCartAPIView.as_view()),
    path('login/', views.UserAPIView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
