"""Define URL pattenrs for users."""

from django.urls import path
from django.contrib.auth import login

from . import views

app_name = 'users'

urlpatterns = [
    # Login Page
    path('login/', views.login_view, name = 'login'),
    # Logout page
    path('logout/', views.logout_view, name = 'logout'),
    # Register page
    path('register/', views.register, name='register'),
]