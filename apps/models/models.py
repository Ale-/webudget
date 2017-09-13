# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# contrib
from djgeojson.fields import PointField
from django_countries.fields import CountryField

class City(models.Model):
    """ City """

    name        = models.CharField(_('Name'), max_length=128, blank=False, null=False, help_text=_('City name. Use native language.'))
    description = models.TextField(_('Summary'), blank=True, help_text=_('A short summary about the city with objective data.'))
    country     = CountryField(_('Country'), help_text=_('Select the country in which the city is located.'))
    coords      = PointField(_('Coordinates'), blank=False, null=True, help_text=_('Locate the city in the map.'))

    class Meta:
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        """ String representation of this model objects. """
        return self.name or '---'

class Dataset(models.Model):
    """ City dataset of a specific year """

    city        = models.ForeignKey(City, verbose_name=_('City'), help_text=_('Select the city related to this dataset'))
    year        = models.PositiveIntegerField(_('Year'), help_text=_('Year of this dataset.'))
    population  = models.PositiveIntegerField(_('Population'), help_text=_('City population.'))
    source      = models.CharField(_('Source'), max_length=128, null=True, help_text=_('Name of the source of the data provided.'))
    source_link = models.URLField(_('Source link'), null=True, help_text=_('A link to the source data provided.'))

    def __str__(self):
        """ String representation of this model objects. """
        return self.city.name + "#" + self.year or '---'
