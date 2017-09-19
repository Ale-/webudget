# django
from django import forms
# apps
from . import models
from apps.utils import widgets as utils

class MunicipalityForm(forms.ModelForm):
    """Form to create/update Municipality objects"""

    class Meta:
        model = models.Municipality
        fields = '__all__'
        widgets = {
            'coords'      : utils.GeocodedLeafletWidget(submit_text='Locate municipality', provider="google", sources="id_name"),
            'description' : utils.LimitedTextareaWidget(limit=500),
        }


    def __init__(self, *args, **kwargs):
        self.base_fields['country'].empty_label = None
        super(MunicipalityForm, self).__init__(*args, **kwargs)
