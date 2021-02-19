from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fortuneTeller-home'),
    path('menu/', views.menu, name='fortuneTeller-menu'),
    path('info/', views.info, name='fortuneTeller-info'),
    path('dailyhoroscope/', views.DailyHoroscope, name='fortuneTeller-info')
]