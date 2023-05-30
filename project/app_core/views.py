from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse_lazy
from app_permissions.models import Sicadfull
from .forms import SicadfullForm

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
from django.shortcuts import render, redirect
from .scripts import adicionar_filtros, collumns_list

@login_required
@user_passes_test(lambda u: u.is_superuser)
def busca(request):
    template = 'busca.html'
    colunas = collumns_list(Sicadfull)
    usuario = request.user

    print(len(colunas))

    if request.method == 'POST':
        query = adicionar_filtros(request)
        resultado = Sicadfull.objects.filter(query)
        context = { "colunas":colunas, "resultado":resultado}
    else:
        context = { "colunas":colunas, }

    
    return render(request, template, context)

@login_required
def edit(request):
    if request.method == 'POST':
        formset = SicadfullForm(request.POST)
        if formset.is_valid():
            formset.save()
            # Faça algo após salvar os dados, se necessário
    else:
        ids = request.POST.getlist('id')  # Obtém uma lista de IDs dos registros selecionados
        sicadfull_objects = []
        for id in ids:
            ocorrencia = Sicadfull.objects.get(id=id)
            if isinstance(ocorrencia, Sicadfull):
                sicadfull_objects.append(ocorrencia)
        
        formset = SicadfullForm(queryset=sicadfull_objects)
    
    return render(request, 'edit.html', {'formset': formset})