from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<id:int>/estados/', views.estados, name='estados'),
]
