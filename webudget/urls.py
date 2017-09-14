# django
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
# project
from apps.views import views

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # i18n
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Contact form
    url(r'^contact/', include('contact_form.urls'))
]

urlpatterns += i18n_patterns(
    # Frontpage
    url(r'^$', TemplateView.as_view(template_name='pages/front.html'), name="front"),
    url(r'', include('registration.backends.default.urls')),
    # Municipality detail
    url(r'^municipality/(?P<slug>[-\w]+)/$', views.MunicipalityDetail.as_view(), name="municipality-detail"),
    # Dataset detail
    # Municipality detail
    url(r'^municipality/(?P<city>[-\w]+)/(?P<year>[-\d]{4})$', views.DatasetDetail.as_view(), name="dataset-detail"),
)

if settings.DEBUG == True:
  urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
  urlpatterns += static( settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT )
