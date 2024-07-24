# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views # Importando a views para urls.py

# -------------------------------------------------------------------------------------------------------------------------------
# LINKS
urlpatterns = [
    path('', views.painelUsuario, name='index'),
    path('entrar/', LoginView.as_view(), name='entrar'),
    path('registrar/', views.registrarUsuario, name='cadastrar'),
    path('alterar/', views.alterarUsuario, name='alterar'),
    path('excluir/', views.excluirUsuario, name='excluir'),
    path('sair/', LogoutView.as_view(next_page='/painel/'), name='sair'),
]