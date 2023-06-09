from django import template
from app_main.lists import GROUP_PERMISSIONS
from django.utils.html import strip_tags

register = template.Library()

@register.filter(name="has_perm")
def has_permission(user, group):
    permissions_groups = GROUP_PERMISSIONS
    for x in permissions_groups:
        if group == x:
            if user.has_perm(f'app_main.{group}'):
                has_perm = True
            else:
                has_perm = False
    return has_perm  

@register.filter(name="get_item")
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def removetags(value, tag):
    return strip_tags(value).replace(tag, '')