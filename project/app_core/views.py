from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse_lazy
from app_permissions.models import Sicadfull

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
from datetime import date
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .scripts import adicionar_argumentos
from django.db.models import Q

@login_required
@user_passes_test(lambda u: u.is_superuser)
def testing(request):
    template = 'template.html'

    colunas = [coluna for coluna in vars(Sicadfull)]

    if request.method == 'POST':
        DATA_INICIO = request.POST.get('data_inicio')
        DATA_FIM = request.POST.get('data_fim')

        print(request.POST)    
    
        args = adicionar_argumentos(DATA_INICIO, DATA_FIM)

        pesquisa = 'joao cleber'
        palavras_chave = pesquisa.split()

        query = Q()
        for palavra in palavras_chave:
            query &= Q(vit_nome__icontains=palavra)

        resultado = Sicadfull.objects.filter(query, **args)

        context = {
            "colunas":colunas,
            "resultado":resultado,
        }
    else:
        context = {
                "colunas":colunas,
            }

    
    return render(request, template, context)