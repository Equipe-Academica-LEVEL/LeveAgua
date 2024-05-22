from django.shortcuts import render, redirect
from conta.forms import Usercreate  # Corrigido o nome do formulário para estar de acordo com a convenção de nomenclatura do Python

def register(request):
    if request.method == 'POST':
        form = Usercreate(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = Usercreate()
    return render(request, 'registration/register.html', {'form': form})
