from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from app_permissions.lists import QUALI_PERMISSIONS, TEMPLATE_PERMISSIONS

@login_required
@user_passes_test(lambda u: u.is_superuser)
def testing(request):
    template = 'template.html'
    all_users = User.objects.all()
    all_permissions = Permission.objects
    perm_groups = TEMPLATE_PERMISSIONS

    if request.method == 'POST' or request.method == 'GET':
        for user in all_users:
            for perm_group in perm_groups:
                permissions = Permission.objects.filter(codename__in=[f'change_{perm_group}',f'view_{perm_group}'])
                name_perm_group = f'{perm_group}_{user.id}'
                
                for permission in permissions:
                    if name_perm_group in request.POST:
                        user.user_permissions.add(permission)
                    else:
                        user.user_permissions.remove(permission)


    context = {
        'all_users': all_users,
        'perm_groups':perm_groups,
    }
    return render(request, template, context)
