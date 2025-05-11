# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.home import views
from django.urls import path
# from .views import homepage_view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.About, name='about'),
    path('index/', views.Index, name='index'),
    path('book/', views.Book, name='book'),
    path('menu/', views.Menu, name='menu'),
 
]

