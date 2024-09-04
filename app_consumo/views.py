# /------------------------------------------------\ #
# | Gerenciamento do consumo de água e faturamento | #
# \------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RelatorioDeConsumoForm, ControleDeIrrigacaoForm
from .models import ControleDeIrrigacao
from django.contrib.auth.decorators import login_required

# -------------------------------------------------------------------------------------------------------------------------------
# PAINEL

# Página principal do Painel com Formulário de Controle de Irrigação integrado
@login_required
def painel(request):
    # Filtra os controles de irrigação do usuário autenticado
    controles_irrigacao = ControleDeIrrigacao.objects.filter(endereco__usuario=request.user)

    # Inicializa o formulário de Controle de Irrigação
    if request.method == 'POST':
        controle_form = ControleDeIrrigacaoForm(request.POST)
        if controle_form.is_valid():
            controle = controle_form.save(commit=False)
            # Atribui o usuário autenticado ao controle através do endereço
            controle.endereco.usuario = request.user
            controle.save()
            return redirect('painel')  # Redirecionar para o painel após salvar
    else:
        controle_form = ControleDeIrrigacaoForm()

    # Inicializa o formulário de Relatório de Consumo
    if request.method == 'POST':
        relatorioCForm = RelatorioDeConsumoForm(request.POST)
        if relatorioCForm.is_valid():
            relatorioCForm.save()
    else:
        relatorioCForm = RelatorioDeConsumoForm()

    # Adiciona os formulários e os controles ao contexto
    contexto = {
        'relatorioCForm': relatorioCForm,
        'controle_form': controle_form,
        'controles_irrigacao': controles_irrigacao,
    }

    return render(request, 'app_consumo_modelos/painel/painel.html', contexto)

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Consumo

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Fatura de Água

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Relatório de Consumo
@login_required
def relatorios(request):
    return HttpResponse("relatorios") # imprimi a string na tela (teste)