from django import template
from BooksFace.BooksFaceApp.models import Profile


register = template.Library()


@register.simple_tag
def check_login(user):
    if isinstance(user, Profile):
        return user.is_authenticated
    return False