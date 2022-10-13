from django import template
from courses.models import *

register = template.Library()


@register.simple_tag()
def get_sections():
    return Sections.objects.all()
