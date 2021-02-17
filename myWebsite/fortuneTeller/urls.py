from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fortuneTeller-home'),
    path('menu/', views.menu, name='fortuneTeller-menu'),
    path('sagittarius/', views.sagittarius, name='fortuneTeller-starSign-sagittarius')
]