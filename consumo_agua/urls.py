from django.urls import path

# Importando a views para urls.py
from . import views

# Define as URLS do Painel (Dashboard) | Consumo de agua
urlpatterns = [
    path('', views.painel, name='index'),
    path('relatorios/', views.relatorios, name='relatorios'),
]