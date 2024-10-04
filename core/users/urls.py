from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('create', views.user_create, name='user_create'),
    path('detail/<int:id>', views.user_detail, name='user_detail'),
    path('user_update/<int:id>', views.user_update, name='user_update'),
    path('delete/<int:id>', views.user_delete, name='user_delete'),
]
