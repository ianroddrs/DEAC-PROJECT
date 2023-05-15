from django import template
from app_permissions.lists import GROUP_PERMISSIONS

register = template.Library()

@register.filter(name="teste")
def has_permission(user, group):
    permissions_groups = GROUP_PERMISSIONS
    for x in permissions_groups:
        if group == x:
            if user.has_perm(f'app_core.view_{group}' and f'app_core.change_{group}'):
                has_perm = True
            else:
                has_perm = False
    return has_perm  