# /-------------------------------------------------------\ #
# | Gerenciamento de Informações dos Usuarios e Endereços | #
# \-------------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from app_usuarios.forms import alterarUsuarioForm, criarUsuarioForm, entrarUsuarioForm, EnderecoForm
from .models import Usuario, Endereco 

# Autenticação
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# JavaScript
from django.http import JsonResponse

# -------------------------------------------------------------------------------------------------------------------------------
# AUTENTICAÇÃO

# Página de cadastro do Usuario (create)
def registrarUsuario(request):
    if request.method == 'POST':
        usuarioCreateForm = criarUsuarioForm(request.POST)
        if usuarioCreateForm.is_valid():
            usuarioCreateForm.save()
            return redirect('entrar')  # Redirecionar para a página inicial ou qualquer outra página após o sucesso
    else:
        usuarioCreateForm = criarUsuarioForm()
    return render(request, 'app_usuarios_modelos/autenticacao/registrar.html', {'usuarioCreateForm': usuarioCreateForm})

# Página de login do Usuario
def entrarUsuario(request):
    form = entrarUsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('painelUsuario')  # Redirecione para a página inicial ou outra página desejada

    return render(request, 'app_usuarios_modelos/autenticacao/entrar.html', {'form': form})

# -------------------------------------------------------------------------------------------------------------------------------
# PAINEL DO USUÁRIO | USUARIO(Atualizar, Ler e Excluir) | ENDEREÇO(Criar, Atualizar, Ler e Excluir)

@login_required
def painelUsuario(request):
    # Visualização e Alteração de Usuario
    usuario_unico = request.user  # Obtém o usuário autenticado

    if request.method == 'POST':
        form_usuario = alterarUsuarioForm(request.POST, instance=usuario_unico)
        form_endereco = EnderecoForm(request.POST, request.FILES)  # Formulário de endereço com suporte para arquivos (imagens)

        if 'salvar_usuario' in request.POST and form_usuario.is_valid():
            form_usuario.save()
            return HttpResponseRedirect('/usuario')

        elif 'adicionar_endereco' in request.POST and form_endereco.is_valid():
            endereco = form_endereco.save(commit=False)
            endereco.usuario = usuario_unico  # Associa o endereço ao usuário logado
            endereco.save()
            return HttpResponseRedirect('/usuario')
    else:
        form_usuario = alterarUsuarioForm(instance=usuario_unico)
        form_endereco = EnderecoForm()  # Formulário vazio para adicionar novo endereço

    # Endereco
    enderecos = Endereco.objects.filter(usuario=usuario_unico)

    # Contexto
    contexto = {
        'form_usuario': form_usuario, 
        'usuario': usuario_unico,
        'enderecos': enderecos,
        'form_endereco': form_endereco,  # Adiciona o formulário de endereço ao contexto
    }
    
    return render(request, 'app_usuarios_modelos/painel/painel.html', contexto)

@login_required
def visualizar_endereco(request, id):
    endereco = get_object_or_404(Endereco, id=id, usuario=request.user)
    
    # Retorna os dados do endereço em formato JSON
    data = {
        'nome_da_propriedade': endereco.nome_da_propriedade,
        'estado': endereco.estado,
        'municipio': endereco.municipio,
        'distrito': endereco.distrito,
        'cep': endereco.cep,
        'complemento': endereco.complemento,
    }
    
    return JsonResponse(data)

def delete(request, endereco_id):
    endereco = get_object_or_404(Endereco, id=endereco_id)
    endereco.delete()
    return redirect('painelUsuario')  # Redirecionar para a página de listagem de endereços
