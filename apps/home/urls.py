# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.home import views
from django.urls import path
# from .views import homepage_view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('home/', views.home_view, name='home'),
    path('report/', views.report_view, name='report'),
    
]

