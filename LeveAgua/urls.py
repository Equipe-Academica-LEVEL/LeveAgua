from django.contrib import admin
from django.urls import path, include

# Define as URLs principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('painel/', include("consumo_agua.urls")), 
    path('usuario/', include("usuarios.urls")),
    path('', include("features.urls")),
]

