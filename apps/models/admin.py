# django
from django.contrib import admin
from django.utils.html import strip_tags
# contrib
from leaflet.admin import LeafletGeoAdmin
from imagekit import ImageSpec
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile
# project
from . import models

# Thumbnail generator for admin views
# @see https://github.com/matthewwithanm/django-imagekit#user-content-admin

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 90 }

def cached_admin_thumb(instance):
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image))
    cached.generate()
    return cached

# Municipality admin form
class MunicipalityAdmin(LeafletGeoAdmin):
    model        = models.Municipality
    ordering     = ('country', 'name',)
    list_display = ('name', 'country', 'description', 'thumb')
    list_filter  = ('country',)
    thumb        = AdminThumbnail(image_field=cached_admin_thumb)
    fields       = (('name', 'country', 'image'), 'description', 'coords')

# Municipality admin form
class DatasetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic data', {
           'fields': (('municipality', 'year', 'population'), ('source', 'source_link'))
        }),
        ('Incomes. Economic classification', {
           'fields': ('in_taxes', 'in_grants', 'in_properties', 'in_fees', 'in_sales', 'in_penalties', 'in_nonfinancial')
        }),
        ('Expenses. Economic classification', {
           'fields': ('ex_wages', 'ex_material', 'ex_financial', 'ex_subsidies', 'ex_grants', 'ex_compensations', 'ex_other', 'ex_nonfinancial')
        }),
        ('COFOG', {
            'fields': ('public_services', 'defence', 'public_order', 'economic_affaris', 'environmental', 'housing', 'health', 'recreation', 'education', 'social_proctection'),
        }),
    )

# Block admin form
class BlockAdmin(admin.ModelAdmin):
    model        = models.Block
    ordering     = ('title',)
    list_display = ('title', 'trimmed_content',)

    def trimmed_content(self, obj):
        txt = strip_tags(obj.body)
        if len(txt) > 200:
            return strip_tags(obj.body)[:200] + "[...]"
        else:
            return txt

# Register models in admin
admin.site.register(models.Municipality, MunicipalityAdmin)
admin.site.register(models.Dataset, DatasetAdmin)
admin.site.register(models.Milestone)
admin.site.register(models.Block, BlockAdmin)
