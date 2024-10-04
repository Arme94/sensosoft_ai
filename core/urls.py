from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('users/', include('core.users.urls')),
    path('reports/', views.reports, name='reports'),
    path('panel/', views.panel, name='panel'),
    path('about/', views.about, name='about'),
    path('who/quienesomos', views.who, name='who')
]
