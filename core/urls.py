from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import get_sensorial_data, save_sensorial_data

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="templates/registration/login.html"), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    
    path('home/', views.home, name='home'),
    path('users/', include('core.users.urls')),
    path('reports/', views.reports, name='reports'),
    path('panel/', views.panel, name='panel'),
    path('about/', views.about, name='about'),
    path('who/quienesomos', views.who, name='who'),
    path('api/get-sensorial-data/', get_sensorial_data, name='get_sensorial_data'),
    path('api/save-sensorial-data/', save_sensorial_data, name='save_sensorial_data'),
    path('api/add-sensory-evaluation/', views.add_sensory_evaluation, name='add_sensory_evaluation'),
    path('api/get-user-info/', views.get_user_info, name='get_user_info')
    
]
