# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.db import models # Necessário para criação de classes
from django.contrib.auth.models import User # Importando a classe "User" do modelo padrão do django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin # Essa é a base do modelo "User"
from django.contrib.auth.models import BaseUserManager

# -------------------------------------------------------------------------------------------------------------------------------
# MANAGER
class UsuarioManager(BaseUserManager):
    def criar_usuario(self, email, nome, sobrenome, cpf, data_nascimento, password=None):
        if not email:
            raise ValueError("O usuário deve ter um email válido")
        if not cpf:
            raise ValueError("O usuário deve ter um CPF válido")
        
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            data_nascimento=data_nascimento,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def criar_superusuario(self, email, nome, sobrenome, cpf, data_nascimento, password=None):
        user = self.criar_usuario(
            email=email,
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


# -------------------------------------------------------------------------------------------------------------------------------
# CLASSES
class Usuario(AbstractBaseUser, PermissionsMixin): # A classe "Usuario" está *herdando* a classe "User"
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True) # "cpf" é CharFIeld para utilização de "." e "-" | também deve ser único (unique=True)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True) # "auto_now_add=True" adiciona automaticamente esse campo

    email = models.EmailField(default='insira o seu email', unique=True)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf', 'data_nascimento']

    def __str__(self):
        return self.email

class Endereco(models.Model): # Classe criada a partir do padrão django "models.Model"
    cep = models.CharField(max_length=9) # "cpf" é CharFIeld para utilização de ".""
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    nome_da_propriedade = models.CharField(max_length=255)
    complemento = models.TextField()
    imagens = models.ImageField(upload_to='enderecos/') #Guarda e utiliza imagens da pasta "enderecos" | Instalar Pillow para seu funcionamento (python -m pip install Pillow) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos') # "Usuario, on_delete=models.CASCADE" significa que o endereço correspondente ao usuário será apagado caso o usuário seja removido