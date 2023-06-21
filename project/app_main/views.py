from django.contrib.auth.models import User, Permission
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Sicadfull
from .lists import GROUP_PERMISSIONS
from .scripts import filtros, columns_list
from datetime import datetime

@login_required
@user_passes_test(lambda u: u.is_superuser)
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
        resultado = Sicadfull.objects.filter(filtros(request.POST))
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
    template = 'editor.html'
    resultados_ids = request.POST.getlist('id')
    colunas = columns_list(Sicadfull)
    ocorrencias = []
    
    for i in resultados_ids:
        ocorrencias.append(Sicadfull.objects.values().get(id=i))

    if request.method == 'POST' and 'salvar' in request.POST.keys():
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

    if request.method == 'POST' and 'editar' in request.POST.keys():
        pass

    context = {
        'colunas':colunas,
        'ocorrencias': ocorrencias,
        'resultados_ids' : resultados_ids,
    }

    return render(request, template, context)
