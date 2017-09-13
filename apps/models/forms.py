# django
from django import forms

class CityForm(forms.ModelForm):

     def __init__(self, *args, **kwargs):
        self.base_fields['country'].empty_label = None
        super(CityForm, self).__init__(*args, **kwargs)
