from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from django.contrib.auth import logout
from django.contrib.contenttypes.models import ContentType


lista_permissions_quali = [
    'nro_tombo','tipo_tombo','controle','consolidado','fato_real',
    'especificacao_crime','meio_emp_deac','distrito','municipios',
    'bairros','atuacao','vit_nome','vit_alcunha','vit_dt_nasc','vit_idade',
    'vit_fx_etaria','vit_nro_doc','vit_tipo_doc','vit_pai','vit_mae',
    'vit_tipo','vit_sexo','vit_cor_pele','vit_grau_inst,vit_profissao',
    'vit_situacao_emprego,vit_estado_civil','aut_nome','aut_alcunha',
    'aut_data_nasc','aut_idade','aut_fx_etaria','aut_nro_doc','aut_tipo_doc',
    'aut_pai','aut_mae','aut_tipo','aut_sexo','grau_de_relacionamento',
    'aut_cor_pele','aut_grau_inst','aut_profissao','aut_sit_emprego',
    'aut_est_civil','meio_locomocao','cor_veiculo','marca_veic_fuga',
    'modelo_do_veic_fuga','qtd_autor','relatorio','ident_autoria','exclusao'
]


@login_required
def home(request):
    template = 'home.html'
    return render(request, template)

@login_required
def sair(request):
    template = 'login.html'
    logout(request)
    return render(request, template)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_permissions(request):
    template = 'permissions.html'
    users = User.objects.all()
    permissions = Permission.objects.all()
    content_type = ContentType.objects.get_for_model(User)
    if request.method == 'POST':
        for user in users:
            for permission in permissions:
                permission_name = 'permission_%s_%s' % (user.id, permission.id)
                if permission_name in request.POST:
                    user.user_permissions.add(permission)
                else:
                    user.user_permissions.remove(permission)
    context = {
        'users': users,
        'permissions': permissions,
        'content_type': content_type,
    }
    return render(request, template, context)




















## test ##
@login_required
def testing(request):
  template = 'template.html'
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return render(request, template, context)