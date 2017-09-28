# django
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponse
# project
from apps.models import models

# Municipality list
class MunicipalityList(ListView):
    model = models.Municipality

    def get_context_data(self, **kwargs):
        context = super(MunicipalityList, self).get_context_data(**kwargs)
        context['current_countries'] = models.Municipality.objects.values("country").distinct()
        return context

# Municipality view
class MunicipalityDetail(DetailView):
    model = models.Municipality

# Dataset view
class DatasetDetail(DetailView):
    model = models.Dataset

    def get(self, request, *args, **kwargs):
        if not self.object:
            raise Http404
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self):
        city = models.Municipality.objects.filter(slug=self.kwargs['city']).first()
        return self.model.objects.filter(year=self.kwargs['year'], municipality=city)
