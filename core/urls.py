from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="templates/registration/login.html"), name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('home/', views.home, name='home'),
    path('users/', include('core.users.urls')),
    path('reports/', views.reports, name='reports'),
    path('panel/', views.panel, name='panel'),
    path('about/', views.about, name='about'),
    path('who/quienesomos', views.who, name='who')
]
