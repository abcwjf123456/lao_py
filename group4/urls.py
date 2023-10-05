from django.urls import path, re_path
from group4 import views

urlpatterns = [
    path('', views.redirect1),
    path('login/', views.redirect_login),
]
