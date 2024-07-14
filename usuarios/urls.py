# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

from django.urls import path

# Importando a views para urls.py
from . import views

# Define as URLS do Usuario
urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.entrar, name='entrar'),
    path('cadastrar/', views.cadastrarUsuario, name='cadastrar'),
    path('alterar/', views.alterarUsuario, name='alterar'),
    path('excluir/', views.excluirUsuario, name='excluir'),
]