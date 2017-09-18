# django
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
# apps
from . import views

urlpatterns = [
    # Add project form
    url(r'^create/municipality$', views.MunicipalityCreate.as_view(), name="create_municipality"),
]
