# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.db import models # Necessário para criação de classes
from django.contrib.auth.models import User # Importando a classe "User" do modelo padrão do django

# -------------------------------------------------------------------------------------------------------------------------------
# CLASSES
class Usuario(User): # A classe "Usuario" está *herdando* a classe "User"
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True) # "cpf" é CharFIeld para utilização de "." e "-" | também deve ser único (unique=True)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True) # "auto_now_add=True" adiciona automaticamente esse campo

    # --------------------------------------------------
    # ATRIBUTOS DA CLASSE "User" EM UTILIZAÇÃO \/
    #
    # email -> EmailField
    # password(senha) -> CharField
    # is_active(ativo/desativado) -> BooleanField (Verdadeiro/Falso)
    # is_superuser(user/superUser) -> BooleanField
    # last_login(último login) -> BooleanField
    # --------------------------------------------------

class Endereco(models.Model): # Classe criada a partir do padrão django "models.Model"
    cep = models.CharField(max_length=9) # "cpf" é CharFIeld para utilização de ".""
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    nome_da_propriedade = models.CharField(max_length=255)
    complemento = models.TextField()
    imagens = models.ImageField(upload_to='enderecos/') #Guarda e utiliza imagens da pasta "enderecos" | Instalar Pillow para seu funcionamento (python -m pip install Pillow) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos') # "Usuario, on_delete=models.CASCADE" significa que o endereço correspondente ao usuário será apagado caso o usuário seja removido