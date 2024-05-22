# urls.py do seu aplicativo de autenticação

from django.contrib.auth.views import LoginView, LogoutView
from conta.views import register
from django.urls import path

app_name = 'conta'  # Definindo o app_name

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
