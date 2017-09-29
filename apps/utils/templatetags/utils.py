# django
from django import template
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# project
from django.conf import settings

register = template.Library()

@register.simple_tag
def css(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/css/' + file

@register.simple_tag
def js(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/js/' + file

@register.simple_tag
def img(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/img/' + file

fake_breadcrumb_default_text = _('Return to previous page')

@register.inclusion_tag('fake-breadcrumb.html')
def fake_breadcrumb(text=fake_breadcrumb_default_text):
    return { 'text' : text }

@register.inclusion_tag('other-blocks/block.html')
def textblock(block=None, display_title=False, title_tag="h3"):
    return { 'block' : block, 'display_title': display_title, 'title_tag' : title_tag }
