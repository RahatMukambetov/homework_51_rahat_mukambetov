from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cat_stats/', views.cat_stats, name='cat_stats'),
]
