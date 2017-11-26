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

# Block admin form
class BlockAdmin(LeafletGeoAdmin):
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
admin.site.register(models.Dataset)
admin.site.register(models.Milestone)
admin.site.register(models.Block, BlockAdmin)
