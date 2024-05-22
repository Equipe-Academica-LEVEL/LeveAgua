# dentro do arquivo de urls do seu projeto

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('conta/', include('conta.urls')),
    path('accounts/', include(auth_urls)),  # sem namespace
]
