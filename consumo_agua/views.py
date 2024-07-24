# /------------------------------------------------\ #
# | Gerenciamento do consumo de água e faturamento | #
# \------------------------------------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RelatorioDeConsumoForm

# Autenticação
from django.contrib.auth.decorators import login_required

# -------------------------------------------------------------------------------------------------------------------------------
# PAINEL

# Página principal do Painel
@login_required
def painel(request):
    # SEÇÕES
    # sessao = 1 -> painel inicial
    # sessao = 2 -> relatorios
    # sessao = 3 -> configuracoes
    sessao = 2

    if request.method == 'POST':
        relatorioCForm = RelatorioDeConsumoForm(request.POST)
        if relatorioCForm.is_valid():
            relatorioCForm.save()
            #return redirect('/painel')  # Redirecionar paraa outra página após o sucesso
    else:
            relatorioCForm = RelatorioDeConsumoForm()
    return render(request, 'painel/painel.html', {'relatorioCForm': relatorioCForm})
    

    """ if sessao == 1:
        return render(request, "painel/painel.html")
    elif sessao == 2:
        if request.method == 'POST':
            relatorioCForm = RelatorioDeConsumoForm(request.POST)
            if relatorioCForm.is_valid():
                relatorioCForm.save()
                #return redirect('/painel')  # Redirecionar paraa outra página após o sucesso
        else:
                relatorioCForm = RelatorioDeConsumoForm()
        return render(request, 'painel/painel.html', {'relatorioCForm': relatorioCForm})
    elif sessao == 3:
        return render(request, "painel/painel.html")
    else:
        return HttpResponse("erro, página não encontrada") """ 


# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Consumo

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Fatura de Água

# -------------------------------------------------------------------------------------------------------------------------------
# CRUD Relatório de Consumo
@login_required
def relatorios(request):
    return HttpResponse("relatorios") # imprimi a string na tela (teste)