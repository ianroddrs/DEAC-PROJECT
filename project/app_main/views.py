from django.contrib.auth.models import User, Permission
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Sicadfull
from .forms import SicadfullForm
from .lists import GROUP_PERMISSIONS
from .scripts import filtros, columns_list

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_permissions(request):
    template = 'permissions.html'
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
    template = 'edit.html'
    resultados_ids = request.POST.getlist('id')
    ocorrencias = []
    form = []
    print(resultados_ids)
    for i in resultados_ids:
        ocorrencias.append(Sicadfull.objects.values().get(id=i))
    for ocorrencia in ocorrencias:
        # print(ocorrencia['id'])
        ocorrencia = Sicadfull.objects.get(id=ocorrencia['id'])
        form.append(SicadfullForm(instance=ocorrencia))
        print(ocorrencia)

    if request.method == 'POST' and 'salvar' in request.POST:
        resultados_ids = request.POST.getlist('id')
        print(resultados_ids,'aaaaaaaaaaaa')
        for f in form:
            print(form)
            if f.is_valid():
                print('valido')
            f.save()
            print('------------------------------------SALVOO------------------------------')

    context = {
        'forms': form,
        'ocorrencias': ocorrencias,
        'resultados': 0
    }

    return render(request, template, context)
