# Bibliotecas
from django.shortcuts import render
from django.http import HttpResponse

# Página principal do Usuario (index)
def index(request):
    return HttpResponse("Pagina do Usuario")

# Página login do Usuario
def entrar(request):
    return HttpResponse("Pagina de login")

# Página cadastro do Usuario
def cadastrar(request):
    return HttpResponse("Pagina de Cadastro")

# Página de alteração do Usuario
def alterar(request):
    return HttpResponse("Pagina de alteração")

# Página de comfirmação de exclusão do Usuario
def comfirmarExcluir(request):
    return HttpResponse("Pagina de comfirmação de exclusão")

# Página de exclusão definitiva
def excluir(request):
    return HttpResponse("Pagina de excluir")