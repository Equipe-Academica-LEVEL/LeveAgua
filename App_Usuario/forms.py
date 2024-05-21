from django import forms
from .models import Modelo_Cliente, Modelo_Administrador, Modelo_Endereco

# Criando Formulario da Classe Cliente
class Formulario_Cliente(forms.ModelForm):
    Senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Modelo_Cliente
        fields = '__all__'

# Criando Formulario da Classe Endereco
class Formulario_Administrador(forms.ModelForm):
    Senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Modelo_Cliente
        fields = '__all__'

# Criando Formulario da Classe Cliente
class Formulario_Endereco(forms.ModelForm):
    class Meta:
        model = Modelo_Cliente
        fields = '__all__'