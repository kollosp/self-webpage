from django.urls import path
from . import views
from django.urls import re_path, include



urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),




]