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
def busca(request):
    template = 'busca.html'
    colunas = collumns_list(Sicadfull)
    usuario = request.user
    if request.method == 'POST':
        values = [value for value in request.POST.items()]
        resultado = Sicadfull.objects.filter(adicionar_filtros(request.POST))
        context = { 
            "colunas":colunas, 
            "resultado":resultado,
            "values":values,
            }
    else:
        context = { 
            "colunas":colunas, 
            }
    return render(request, template, context)




@login_required
def edit(request):
    template = 'edit.html'
    resultados_ids = request.POST.getlist('id')
    ocorrencias = []
    form = []
    print(resultados_ids)
    if request.method == 'POST' and 'salvar' in request.POST:
        resultados_ids = request.POST.getlist('id')
        print(resultados_ids,'aaaaaaaaaaaa')
        for i in resultados_ids:
            ocorrencias.append(Sicadfull.objects.values().get(id=i))
        
        for ocorrencia in ocorrencias:
            ocorrencia = Sicadfull.objects.get(id=ocorrencia['id'])
            form.append(SicadfullForm(instance=ocorrencia))
            print(form[0])
        # if all([f.is_valid() for f in form]):
        for f in form:
            # if f.is_valid():
            #     print('valido')
            f.save()
            print('------------------------------------SALVOO------------------------------')
            # return redirect(busca)
    else:
        for i in resultados_ids:
            ocorrencias.append(Sicadfull.objects.values().get(id=i))
        for ocorrencia in ocorrencias:
            # print(ocorrencia['id'])
            ocorrencia = Sicadfull.objects.get(id=ocorrencia['id'])
            form.append(SicadfullForm(instance=ocorrencia))
            print(form)
    
    context = {
        'form': form,
        'ocorrencias': ocorrencias,
        'resultados': 0
    }

    return render(request, template, context)
