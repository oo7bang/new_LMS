from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('', views.manager_view),
    path('', views.client_view),
]
