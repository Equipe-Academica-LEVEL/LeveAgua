from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import appForm
from .models import app

@login_required
def criar(request):
    if request.method == 'POST':
        form = appForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/?msg=Salvo')
    else:
        form = appForm()
    return render(request, 'app/form.html', {'Form': form})

@login_required
def listarTudo(request):
    user = request.user.username
    alunos = app.objects.all()
    return render(request, "app/listarTudo.html", {'app': alunos})

@login_required
def editar(request, id_app):
    apps = app.objects.get(pk=id_app)
    if request.method == 'POST':
        form = appForm(request.POST, instance=apps)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/?msg=Salvo')
    else:
        form = appForm(instance=apps)
    return render(request, 'app/update.html', {'Form': form, 'id_app': id_app})

@login_required
def deletar(request, id_app):
    apps = app.objects.get(pk=id_app)
    apps.delete()
    return HttpResponseRedirect('/app/?msg=Apagado')

@login_required
def delete(request, id_app):
    apps = app.objects.get(pk=id_app)    
    return render(request, 'app/delete.html', {'app': apps})

@login_required
def detail(request, id_app):
    try:
        saida = app.objects.get(pk=id_app)
    except:
        saida = 'Aqui não tem aluno!'
    return render(request, 'app/index.html', {'app': saida})

@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/?msg=Usuário criado com sucesso!')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
