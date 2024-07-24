# /------------------------------------------------\ #
# | Gerenciamento do consumo de água e faturamento | #
# \------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Endereco

# Extendendo a classe UserAdmin para adicionar campos personalizados
class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('sobrenome', 'cpf', 'data_nascimento', 'data_criacao')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('sobrenome', 'cpf', 'data_nascimento', 'email', 'username', 'password1', 'password2')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'cpf', 'data_nascimento']

# Registro do modelo Usuario
admin.site.register(Usuario, UsuarioAdmin)