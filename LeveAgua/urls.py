from django.contrib import admin
from django.urls import path, include

# Define as URLs principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App_Pag_Inicial.urls")), 
    path('Painel/', include("App_Painel.urls")), 
    path('Usuario/', include("App_Usuario.urls")),
]
