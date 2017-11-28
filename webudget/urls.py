# django
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
# project
from apps.views import views
from apps.models import urls as models_urls

urlpatterns = [
    # i18n
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Contact form
    url(r'^contact/', include('contact_form.urls')),
    # CKEditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # Registration
    url(r'', include('registration.backends.default.urls')),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Api test
    url(r'^api/test$', views.ApiTest, name="api-test"),
]

urlpatterns += i18n_patterns(
    # Forms
    url(r'', include(models_urls, namespace="modelforms")),
    # Frontpage
    url(r'^$', views.Front.as_view(), name="front"),
    # Static
    # About
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    # Credits
    url(r'^credits/$', TemplateView.as_view(template_name='pages/credits.html'), name="credits"),
    # Terms
    url(r'^terms/$', TemplateView.as_view(template_name='pages/terms.html'), name="terms"),
    # Privacy
    url(r'^privacy/$', TemplateView.as_view(template_name='pages/privacy.html'), name="privacy"),
    # Municipality list
    url(r'^municipalities/', views.MunicipalityList.as_view(), name="municipality-list"),
    # Municipality detail
    url(r'^municipality/(?P<slug>[-\w]+)/$', views.MunicipalityDetail.as_view(), name="municipality-detail"),
    # Dataset detail
    # Municipality detail
    url(r'^municipality/(?P<city>[-\w]+)/(?P<year>[-\d]{4})$', views.DatasetDetail.as_view(), name="dataset-detail"),
    # Participate
    url(r'^participate/$', TemplateView.as_view(template_name='pages/participate.html'), name="participate"),    
)

if settings.DEBUG == True:
  urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
  urlpatterns += static( settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT )
