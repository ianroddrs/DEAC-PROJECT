from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse_lazy

@login_required
def home(request):
    template = 'home.html'
    return render(request, template)

@login_required
def sair(request):
    template = 'login'
    logout(request)
    return redirect(reverse_lazy(template))





## test ##
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app_permissions.lists import GROUP_PERMISSIONS

@login_required
@user_passes_test(lambda u: u.is_superuser)
def testing(request):
    template = 'template.html'

    colunas = [
        'Numero de Boletin',
        'Numero de Procedimento',
        'Relato',
        'Municipio',
        'Bairro',
        'Data Inicio',
        'Data Fim',
        'Nome do Autor',
        'Nome da Vitima',
        'Procedimento',
        'Meio Empregado',
        'Meio de Locomoção',
    ]

    if request.method == 'POST':
        pass

    context = {
        "colunas":colunas,
    }
    
    return render(request, template, context)