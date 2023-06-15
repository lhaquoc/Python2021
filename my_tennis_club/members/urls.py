from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('testing', views.testing, name='testing')
]
