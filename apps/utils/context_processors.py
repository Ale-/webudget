# apps
from django.conf import settings

def html_document_meta(request):
    """Injects the name of current user in site-wide context"""

    html_document_title       = settings.DOCUMENT_TITLE
    html_document_description = settings.DOCUMENT_DESCRIPTION

    return locals()
