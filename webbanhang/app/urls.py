from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction/', views.introduction, name='introduction'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout')
]
