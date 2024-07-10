# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render
from django.http import HttpResponse

# -------------------------------------------------------------------------------------------------------------------------------
# PÁGINAS

# Página login do Usuario
def entrar(request):
    return HttpResponse("Pagina de login") # imprimi a string na tela (teste)

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Usuário

# Página principal do Usuario (index | read)
def index(request):
    return HttpResponse("Pagina do Usuario") # imprimi a string na tela (teste)

# Página cadastro do Usuario (create)
def cadastrar(request):
    return HttpResponse("Pagina de Cadastro") # imprimi a string na tela (teste)

# Página de alteração do Usuario (update)
def alterar(request):
    return HttpResponse("Pagina de alteração") # imprimi a string na tela (teste)

# Página de comfirmação de exclusão do Usuario (confirm delete)
def comfirmarExcluir(request):
    return HttpResponse("Pagina de comfirmação de exclusão") # imprimi a string na tela (teste)

# Página de exclusão definitiva (Delete)
def excluir(request):
    return HttpResponse("Pagina de excluir") # imprimi a string na tela (teste)

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Endereço