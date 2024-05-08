# Bibliotecas
from django.shortcuts import render
from django.http import HttpResponse

# Página principal do Painel (index)
def index(request):
    return HttpResponse("Painel")