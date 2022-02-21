from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path(r'login/', views.login_view),
    path(r'manager/', views.manager_view),
    path(r'client/', views.client_view),
    path(r'detect_me/', views.detect_me, name='detect_me')
]
