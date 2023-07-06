from django.contrib.auth.models import User, Permission
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Sicadfull
from .lists import GROUP_PERMISSIONS
from .scripts import filtros, columns_list
from datetime import datetime
from django.shortcuts import redirect

@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['Gerente', 'Administrador']).exists())
def user_permissions(request):
    template = 'permissoes.html'
    users = User.objects.all()
    groups = GROUP_PERMISSIONS

    if request.method == 'POST':
        for user in users:
            user.user_permissions.clear()
            for group in groups:
                permission_name = '%s_%s' % (group, user.id)
                if permission_name in request.POST:
                    permission_selects = Permission.objects.filter(codename__in=[group])
                    for permission in permission_selects:
                        user.user_permissions.add(permission)

    context = {
        'users': users,
        'groups': groups,
    }
    
    return render(request, template, context)

@login_required
def busca(request):
    template = 'busca.html'
    colunas = columns_list(Sicadfull)
    usuario = request.user
    if request.method == 'POST':
        values = [value for value in request.POST.items()]
        Boletins = Sicadfull.objects.filter(filtros(request.POST))
        context = { 
            "colunas":colunas, 
            "Boletins":Boletins,
            "values":values,
            }
    else:
        context = { 
            "colunas":colunas, 
            }
    return render(request, template, context)


@login_required
def editor(request):
    template = 'editor.html'
    colunas = columns_list(Sicadfull)
    ocorrencias = []
    resultados_ids = []

    if request.method == 'POST':
        
        resultados_ids = request.POST.getlist('id')
        for i in resultados_ids:
            ocorrencias.append(Sicadfull.objects.values().get(id=i))
            
        if 'editar' in request.POST.keys():
            Boletins = Sicadfull.objects.filter(filtros(request.POST))
            resultados_ids = list(Boletins.values_list('id', flat=True))
        elif 'salvar' in request.POST.keys():
            for ocorrencia in ocorrencias:
                obj_id = ocorrencia['id']
                obj = get_object_or_404(Sicadfull, id=obj_id)
                for col in colunas:
                    novo_valor = request.POST.get(f"coll_{obj_id}_{col}")
                    print(col, ": ", novo_valor)
                    if novo_valor == '' or novo_valor == 'None':
                        novo_valor = None
                    if col == 'exclusao' and novo_valor == 'on':
                        novo_valor = True
                    setattr(obj, col, novo_valor)
                obj.save()
        if len(resultados_ids) == 1:
            return redirect('edit_line',id=resultados_ids[0])


    context = {
        'colunas':colunas,
        'ocorrencias': ocorrencias,
        'resultados_ids' : resultados_ids,
    }

    return render(request, template, context)


@login_required
def edit_line(request, id):

    template = 'edit_line.html'
    boletim = Sicadfull.objects.values().get(id=id)

    if request.method == 'POST':
        print("foi")

    
    context = {
        'id' : id,
        'boletim':boletim,
    }

    return render(request, template, context)