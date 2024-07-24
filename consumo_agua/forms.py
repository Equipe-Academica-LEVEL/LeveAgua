# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django import forms
from .models import RelatorioDeConsumo, FaturaAgua, Consumo 

# -------------------------------------------------------------------------------------------------------------------------------
# FORMULARIOS

# Formulário utilizado na views do app painel
class RelatorioDeConsumoForm(forms.ModelForm):
    class Meta:
        model = RelatorioDeConsumo
        fields = ['periodo', 'modelo', 'consumo']
