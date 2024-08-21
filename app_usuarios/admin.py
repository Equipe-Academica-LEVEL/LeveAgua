# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from app_usuarios.forms import criarUsuarioForm, alterarUsuarioForm

# -------------------------------------------------------------------------------------------------------------------------------
# FORMULÁRIOS ADMIN
class UsuarioAdmin(BaseUserAdmin):
    ordering = ['email']
    search_fields = ('email', 'nome', 'sobrenome', 'cpf')

    add_form = criarUsuarioForm
    form = alterarUsuarioForm
    model = Usuario

    list_display = ['email', 'nome', 'sobrenome', 'is_active'] # Campos que serão mostrados na listagem do Django Admin.
    list_filter = ['is_active']

    # Configurações das seções de campos exibidos na página de detalhes de um usuário. Aqui você especifica os campos que realmente existem no modelo Usuario
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'sobrenome', 'cpf', 'data_nascimento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'sobrenome', 'cpf', 'data_nascimento', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)