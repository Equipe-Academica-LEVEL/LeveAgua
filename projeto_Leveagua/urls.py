# /-----------------------------------------\ #
# | Gerenciamento de URLs Gerais do Projeto | #
# \-----------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib import admin
from django.urls import path, include

# -------------------------------------------------------------------------------------------------------------------------------
# LINKS
urlpatterns = [
    path('', include("app_features.urls")),
    path('admin/', admin.site.urls), 
    path('usuario/', include("app_usuarios.urls")),
    path('painel/', include("app_consumo.urls")),
]