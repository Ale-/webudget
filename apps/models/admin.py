# django
from django.utils.translation import ugettext_lazy as _
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

# Dataset admin form

dataset_fields = models.Dataset._meta.get_fields()
def cofog_fields(cat):
    return  [ str(field)[15:] for field in dataset_fields if str(field).startswith('models.Dataset.concept_' + cat) ]

class DatasetAdmin(admin.ModelAdmin):

    fieldsets    = (
        (_('General data'), {
            'fields' : ['municipality', 'year', 'population', ('source', 'source_link') ],
        }),
        (_('General public services'), {
            'fields' : cofog_fields('ps'),
            'classes': ('collapse',),
        }),
        (_('Defence'), {
            'fields' : cofog_fields('de')
        }),
        (_('Public order and safety'), {
            'fields' : cofog_fields('po')
        }),
        (_('Economic affairs'), {
            'fields' : cofog_fields('ea')
        }),
        (_('Environmental protection'), {
            'fields' : cofog_fields('ep')
        }),
        (_('Housing and community amenities'), {
            'fields' : cofog_fields('ho')
        }),
        (_('Health'), {
            'fields' : cofog_fields('he')
        }),
        (_('Recreation, culture and religion'), {
            'fields' : cofog_fields('re')
        }),
        (_('Education'), {
            'fields' : cofog_fields('ed')
        }),
        (_('Social protection'), {
            'fields' : cofog_fields('so')
        }),
    )

    class Media:
        js = (
            'webudget/js/dataset-admin.js',       # project static folder
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
