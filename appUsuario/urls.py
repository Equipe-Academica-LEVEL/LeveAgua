from django.urls import path

# Importando a views para urls.py
from . import views

# Define as URLS do Usuario
urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.index, name='entrar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('alterar/', views.alterar, name='alterar'),
    path('excluir/', views.comfirmarExcluir, name='excluir'),
]