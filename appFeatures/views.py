# Bibliotecas
from django.shortcuts import render
from django.http import HttpResponse

# Página Inicial (index)
def index(request):
    return render(request, "Pag_Inicial/Pag_Inicial.html")