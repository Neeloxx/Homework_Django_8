from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag(name='current_date')
def current_date(date_format='%b %d %Y'):
    return datetime.utcnow().strftime(date_format)