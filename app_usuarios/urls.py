# /------------------------------------------------\ #
# | Gerenciamento de URLs dos Usuarios e Endereços | #
# \------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views # Importando a views para urls.py

# -------------------------------------------------------------------------------------------------------------------------------
# LINKS
urlpatterns = [
    path('', views.painelUsuario, name='painelUsuario'),
    path('entrar/', views.entrarUsuario, name='entrar'),
    path('registrar/', views.registrarUsuario, name='cadastrar'),
    path('sair/', LogoutView.as_view(next_page='/'), name='logout'),
    path('usuario/endereco/<int:id>/', views.visualizar_endereco, name='visualizar_endereco'),
    path("delete/<int:endereco_id>/", views.delete, name="delete"),
]