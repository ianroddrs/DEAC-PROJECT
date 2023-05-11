from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from .lists import lista_permissions_template, lista_permissions_quali

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_permissions(request):
    template = 'permissions.html'
    users = User.objects.all()
    permissions = Permission.objects.all()

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
    }
    return render(request, template, context)
