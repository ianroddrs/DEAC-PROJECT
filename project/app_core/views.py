from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    template = 'home.html'
    return render(request, template)

@login_required
def sair(request):
    template = 'login.html'
    logout(request)
    return render(request, template)

## test ##
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from app_permissions.lists import QUALI_PERMISSIONS, TEMPLATE_PERMISSIONS

@login_required
@user_passes_test(lambda u: u.is_superuser)
def testing(request):
    template = 'template.html'
    users = User.objects.all()
    permissions = Permission.objects.all()
    perm_groups = TEMPLATE_PERMISSIONS

    if request.method == 'POST':
        for user in users:
            for permission, perm_group in zip(permissions, perm_groups):
                permission_name = 'permission_%s_%s' % (user.id, permission[1].id)
                if permission_name in request.POST:
                    user.user_permissions.add(permission)
                else:
                    user.user_permissions.remove(permission)

    context = {
        'users': users,
        'permissions': permissions,
        'perm_groups':perm_groups,
    }
    return render(request, template, context)
