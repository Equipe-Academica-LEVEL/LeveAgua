# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django import forms
from .models import Usuario, Endereco
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


# -------------------------------------------------------------------------------------------------------------------------------
# FORMULÁRIOS

# Criação de Usuário
class criarUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        help_text="Sua senha deve ter pelo menos 8 caracteres.",
    )
    password2 = forms.CharField(
        label='Repita a Senha',
        widget=forms.PasswordInput,
        help_text="Repita a mesma senha para verificação.",
    )

    # Configura o campo "data_nascimento" para usar um input HTML5 do tipo "date"
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'sobrenome', 'cpf', 'data_nascimento')

    def __init__(self, *args, **kwargs):
        super(criarUsuarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form' #Adiciona a classe 'label-form'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coecidem")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
# -------------------------------------------------------------------------------------------------------------------------------
# Alterar Usuário
class alterarUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput,
        required=False,  # Tornando opcional, pois o usuário pode não querer alterar a senha
        help_text="Deixe em branco se não quiser alterar a senha."
    )
    password2 = forms.CharField(
        label='Repita a Nova Senha',
        widget=forms.PasswordInput,
        required=False,  # Tornando opcional
        help_text="Repita a mesma senha para verificação."
    )

    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'cpf', 'data_nascimento')

    def __init__(self, *args, **kwargs):
        super(alterarUsuarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'label-form'  # Adiciona a classe 'label-form'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get("password1")
        if password1:  # Se uma nova senha foi fornecida, altere a senha do usuário
            user.set_password(password1)
        if commit:
            user.save()
        return user


# Login do Usuário
class entrarUsuarioForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'label-form'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'label-form'}), label="Senha")

    def __init__(self, *args, **kwargs):
        super(entrarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha'

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Email ou senha incorretos.")
        return self.cleaned_data

    def get_user(self):
        return self.user

# Endereços do Usuário
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['nome_da_propriedade', 'cep', 'municipio', 'estado', 'distrito', 'complemento']
        labels = {
            'cep': 'Código Postal',
        }
    
    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        
        # Ordenando o campo "nome_da_propriedade" para ser o primeiro
        self.fields['nome_da_propriedade'].widget.attrs.update({'class': 'label-form'})
        self.fields['cep'].widget.attrs.update({'class': 'label-form'})
        self.fields['municipio'].widget.attrs.update({'class': 'label-form'})
        self.fields['estado'].widget.attrs.update({'class': 'label-form'})
        self.fields['distrito'].widget.attrs.update({'class': 'label-form'})
        self.fields['complemento'].widget.attrs.update({'class': 'label-form'})

        # Campos como select com valor padrão
        self.fields['municipio'].widget = forms.Select(choices=[(self.instance.municipio, self.instance.municipio)])
        self.fields['estado'].widget = forms.Select(choices=[(self.instance.estado, self.instance.estado)])
        self.fields['distrito'].widget = forms.Select(choices=[(self.instance.distrito, self.instance.distrito)])

        # Predefine o valor do campo "cep" como vazio (será preenchido dinamicamente)
        self.fields['cep'].widget.attrs['readonly'] = True  # Definido como readonly para que não possa ser alterado manualmente

    def clean(self):
        cleaned_data = super().clean()
        distrito = cleaned_data.get("distrito")

        # Verifica se o distrito é "Ceraima" e define o código postal correspondente
        if distrito == "Ceraima":
            cleaned_data['cep'] = "46433-971"

        return cleaned_data

    def save(self, commit=True, user=None):
        endereco = super().save(commit=False)
        if user:
            endereco.usuario = user  # Atribui o usuário autenticado
        if commit:
            endereco.save()
        return endereco
    
class alterarEnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['nome_da_propriedade', 'cep', 'municipio', 'estado', 'distrito', 'complemento']
        labels = {
            'cep': 'Código Postal',
        }
    
    def __init__(self, *args, **kwargs):
        super(alterarEnderecoForm, self).__init__(*args, **kwargs)
        
        # Ordenando o campo "nome_da_propriedade" para ser o primeiro
        self.fields['nome_da_propriedade'].widget.attrs.update({'class': 'label-form editar_nome_da_propriedade'})
        self.fields['cep'].widget.attrs.update({'class': 'label-form editar_cep'})
        self.fields['municipio'].widget.attrs.update({'class': 'label-form editar_municipio'})
        self.fields['estado'].widget.attrs.update({'class': 'label-form editar_estado'})
        self.fields['distrito'].widget.attrs.update({'class': 'label-form editar_distrito'})
        self.fields['complemento'].widget.attrs.update({'class': 'label-form editar_complemento'})

        # Campos como select com valor padrão
        self.fields['municipio'].widget = forms.Select(choices=[(self.instance.municipio, self.instance.municipio)])
        self.fields['estado'].widget = forms.Select(choices=[(self.instance.estado, self.instance.estado)])
        self.fields['distrito'].widget = forms.Select(choices=[(self.instance.distrito, self.instance.distrito)])

        # Predefine o valor do campo "cep" como vazio (será preenchido dinamicamente)
        self.fields['cep'].widget.attrs['readonly'] = True  # Definido como readonly para que não possa ser alterado manualmente

    def clean(self):
        cleaned_data = super().clean()
        distrito = cleaned_data.get("distrito")

        # Verifica se o distrito é "Ceraima" e define o código postal correspondente
        if distrito == "Ceraima":
            cleaned_data['cep'] = "46433-971"

        return cleaned_data

    def save(self, commit=True, user=None):
        endereco = super().save(commit=False)
        if user:
            endereco.usuario = user  # Atribui o usuário autenticado
        if commit:
            endereco.save()
        return endereco