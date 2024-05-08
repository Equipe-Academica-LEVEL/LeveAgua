# Bibliotecas
from django.shortcuts import render
from django.http import HttpResponse

# Página principal do Usuario (index)
def index(request):
    return HttpResponse("Pagina do Usuario")