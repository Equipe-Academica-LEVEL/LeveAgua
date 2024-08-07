# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views # Importando a views para urls.py

# -------------------------------------------------------------------------------------------------------------------------------
# LINKS
urlpatterns = [
    path('', views.painelUsuario, name='index'),
    path('login/', auth_views.LoginView.as_view, name='login'),
    path('registrar/', views.registrarUsuario, name='cadastrar'),
    path('sair/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]