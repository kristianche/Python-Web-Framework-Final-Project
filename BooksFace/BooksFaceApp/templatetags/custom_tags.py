from django import template
from BooksFace.BooksFaceApp.models import Profile
from django.contrib.auth.models import Group

register = template.Library()


@register.filter
def in_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False