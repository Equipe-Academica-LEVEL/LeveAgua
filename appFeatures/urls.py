from django.urls import path

# Importando a views para urls.py
from . import views

# Define a URL da Pagina Inicial
urlpatterns = [
    path('', views.index, name='index'),
]