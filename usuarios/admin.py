from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from usuarios.forms import criarUsuarioForm, alterarUsuarioForm

class UsuarioAdmin(BaseUserAdmin):
    ordering = ['email']

    add_form = criarUsuarioForm
    form = alterarUsuarioForm
    model = Usuario
    list_display = ['email', 'nome', 'sobrenome', 'is_active']
    list_filter = ['is_active']

admin.site.register(Usuario, UsuarioAdmin)