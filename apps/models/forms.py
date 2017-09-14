# django
from django import forms

class MunicipalityForm(forms.ModelForm):

     def __init__(self, *args, **kwargs):
        self.base_fields['country'].empty_label = None
        super(MunicipalityForm, self).__init__(*args, **kwargs)
