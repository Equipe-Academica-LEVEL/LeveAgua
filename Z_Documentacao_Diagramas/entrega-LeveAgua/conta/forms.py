from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Usercreate(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',  
             'password1', 'password2',
        ]


    first_name = forms.CharField(
        label="Nome"
    )
    last_name = forms.CharField(
        label="Sobrenome" 
    )    
    username = forms.CharField(
        label="Username"
    )
    email = forms.CharField(
        label="Email"
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput
    )