from django import template

from quizes.models import Quiz

register = template.Library()


@register.simple_tag()
def categories():
    return Quiz.objects.all()