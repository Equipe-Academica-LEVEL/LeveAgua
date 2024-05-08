from django.urls import path

# Importando a views para urls.py
from . import views

# Define as URLS do Painel (Dashboard)
urlpatterns = [
    path('', views.index, name='index'),
]