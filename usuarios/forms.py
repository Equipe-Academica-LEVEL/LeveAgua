# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Endereco

# -------------------------------------------------------------------------------------------------------------------------------
# FORMULÁRIOS

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','nome', 'sobrenome', 'cpf', 'email', 'data_nascimento','password1', 'password2']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'municipio', 'estado', 'nome_da_propriedade', 'complemento', 'imagens', 'usuario']
