#Bibliotecas
from django.db import models
import django.contrib.auth


# Criando classe generalizada (Usuário)
class Classe_Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=20)
    cpf = models.IntegerField(14)
    dataDeNascimento = models.DateField()

# Criando classe Endereço | Diretemente ligada com o cliente (indica sua propriedade)
class Classe_Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Classe_Usuario,  on_delete=models.CASCADE)
    municipio = models.CharField(max_length=50, default="Guanambi")
    distrito = models.CharField(max_length=50, default="Ceraima")
    cep = models.IntegerField(9, default=46433.000)
    nomeDaPropriedade = models.CharField(max_length=100)
    complemento = models.TextField(max_length=50)
    imagens = models.ImageField(upload_to='Arquivos_Static/Imagens_ModeloEndereco')
