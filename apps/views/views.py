# python
import json
from random import randint
# django
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponse
# project
from apps.models import models

# Frontpage
class Front(View):
    def get(self, request, *args, **kwargs):
        municipalities = models.Municipality.objects.all()
        presentation   = models.Block.objects.get(title="Presentation")
        return render(request, 'pages/front.html', locals())

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


# Dataset fake API for testing D3 widgets
def ApiTest(request):
    datasets = []
    # Fetch COFOG related fields
    dataset_fields = models.Dataset._meta.get_fields()
    cofog_fields   = [ field for field in dataset_fields if str(field).startswith('models.Dataset.concept_') ]
    for i in range(17):
        dataset = { 'year' : 2000 + i }
        for field in cofog_fields:
            dataset[str(field.verbose_name)] = randint(2e6, 20e6)
        datasets.append(dataset)

    return HttpResponse(json.dumps(datasets), content_type="application/json")
