# django
from django.contrib import admin
# contrib
from leaflet.admin import LeafletGeoAdmin
# project
from . import models

# Register models in admin
admin.site.register(models.City, LeafletGeoAdmin)
admin.site.register(models.Dataset)
admin.site.register(models.Milestone)
