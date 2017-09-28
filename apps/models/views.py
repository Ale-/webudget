# django
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.utils.html import escape
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
# apps
from apps.models import forms, models

normal_template = 'pages/modelform.html'
delete_template = 'pages/modelform--delete.html'

class MunicipalityCreate(LoginRequiredMixin, CreateView):
    """ Form to add municipalities """

    form_class    = forms.MunicipalityForm
    model         = models.Municipality
    template_name = normal_template

    def get_context_data(self, **kwargs):
        context = super(MunicipalityCreate, self).get_context_data(**kwargs)
        context['title'] = _('Add a municipality to database')
        context['form_html_class'] = 'municipality'
        context['submit_text'] = _('Add municipality')
        return context

    def get_success_url(self):
        return reverse('municipality-list')
