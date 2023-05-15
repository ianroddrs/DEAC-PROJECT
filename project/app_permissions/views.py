from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Permission
from .lists import GROUP_PERMISSIONS

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_permissions(request):
    template = 'template.html'
    users = User.objects.all()
    groups = GROUP_PERMISSIONS

    if request.method == 'POST':
        for user in users:
            user.user_permissions.clear()
            for group in groups:
                permission_name = '%s_%s' % (group, user.id)
                if permission_name in request.POST:
                    permission_selects = Permission.objects.filter(codename__in=[f'change_{group}', f'view_{group}'])
                    for permission in permission_selects:
                        user.user_permissions.add(permission)
                        
    context = {
        'users': users,
        'groups': groups,
    }
    return render(request, template, context)
