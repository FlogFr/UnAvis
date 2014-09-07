"""
tags py for the templating pages
"""

import re
from django import template
from django.template import Library
from Core.models import Category

register = Library()

import logging
logger = logging.getLogger(__name__)


@register.simple_tag
def active(request, pattern, *args, **kwargs):
    if re.search(pattern, request.path):
        return 'active'
    return ''


class CategoryNode(template.Node):
    def __init__(self, context_name, user=None):
        self.context_name = context_name

    def render(self, context):
        context[self.context_name] = Category.objects.all()
        return ''


@register.tag
def get_categories(parser, token):
    """
    Retrieves all the categories url
    """
    bits = token.split_contents()
    syntax_message = ("%(tag_name)s expects a syntax of %(tag_name)s "
                      "['url_starts_with'] [for user] as context_name" %
                      dict(tag_name=bits[0]))
    if bits[-2] != 'as':
        raise template.TemplateSyntaxError(syntax_message)
    if bits[-4] == 'for':
        user = bits[-3]
    else:
        user = None
    context_name = bits[-1]
    return CategoryNode(context_name, user=user)
