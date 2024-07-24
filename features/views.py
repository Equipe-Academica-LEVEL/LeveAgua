# /--------------------\ #
# | Ferramentas Extras | #
# \--------------------/ #

# -------------------------------------------------------------------------------------------------------------------------------
# IMPORTAÇÕES
from django.shortcuts import render
from django.http import HttpResponse

# -------------------------------------------------------------------------------------------------------------------------------
# PÁGINAS

# Página login do Usuario
def pagina_inicial(request):
    if request.user.is_authenticated:
        # O usuário está logado
        logado = True
        return render(request, "pag_inicial/inicio.html", {'logado': logado})
    else:
        # O usuário não está logado
        logado = False
        return render(request, "pag_inicial/inicio.html", {'logado': logado})