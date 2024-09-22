from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('users/create', views.user_create, name='user_create'),
    path('users/detail/<int:id>', views.user_detail, name='user_detail'),
    path('users/user_update/<int:id>', views.user_update, name='user_update'),
    path('users/delete/<int:id>', views.user_delete, name='user_delete'),
    path('reports/', views.reports, name='reports'),
    path('panel/', views.panel, name='panel'),
    path('about/', views.about, name='about'),
]
