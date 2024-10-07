from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.users), name='users'),
    path('create', login_required(views.user_create), name='user_create'),
    path('detail/<int:id>', login_required(views.user_detail), name='user_detail'),
    path('user_update/<int:id>', login_required(views.user_update), name='user_update'),
    path('delete/<int:id>', login_required(views.user_delete), name='user_delete'),
]
