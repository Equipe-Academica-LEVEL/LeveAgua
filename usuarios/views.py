# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.forms import UsuarioForm

# Autenticação
from django.contrib.auth.decorators import login_required

# -------------------------------------------------------------------------------------------------------------------------------
# PÁGINAS

# Página login do Usuario (NÃO ESTÁ SENDO USADA NO MOMENTO)
def entrar(request):
    return HttpResponse("Pagina de login") # imprimi a string na tela (teste)

# Página principal do Usuario (index | read) / Endereço incluso
@login_required
def painelUsuario(request):
    return render(request, 'usuario/painel-usuario.html')

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Usuário

# Página cadastro do Usuario (create)
def registrarUsuario(request):
    if request.method == 'POST':
        usuarioCreateForm = UsuarioForm(request.POST)
        if usuarioCreateForm.is_valid():
            usuarioCreateForm.save()
            return redirect('painelUsuario')  # Redirecionar para a página inicial ou qualquer outra página após o sucesso
    else:
        usuarioCreateForm = UsuarioForm()
    return render(request, 'registration/register.html', {'usuarioCreateForm': usuarioCreateForm})

# Página de alteração do Usuario (update)
@login_required
def alterarUsuario(request):
    return HttpResponse("Pagina de alteração") # imprimi a string na tela (teste)

# Página de exclusão definitiva (Delete)
@login_required
def excluirUsuario(request):
    return HttpResponse("Pagina de excluir") # imprimi a string na tela (teste)

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Endereço

# Página cadastro do Usuario (create)
@login_required
def cadastrar(request):
    return HttpResponse("Pagina de Cadastro") # imprimi a string na tela (teste)

# Página de alteração do Usuario (update)
@login_required
def alterar(request):
    return HttpResponse("Pagina de alteração") # imprimi a string na tela (teste)

# Página de comfirmação de exclusão do Usuario (confirm delete)
@login_required
def comfirmarExcluir(request):
    return HttpResponse("Pagina de comfirmação de exclusão") # imprimi a string na tela (teste)

# Página de exclusão definitiva (Delete)
@login_required
def excluir(request):
    return HttpResponse("Pagina de excluir") # imprimi a string na tela (teste)