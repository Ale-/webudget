# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
# contrib
from djgeojson.fields import PointField
from django_countries.fields import CountryField

class Municipality(models.Model):
    """ Municipality """

    name        = models.CharField(_('Name'), max_length=128, blank=False, null=False, help_text=_('Municipality name. Use native language.'))
    description = models.TextField(_('Summary'), blank=True, help_text=_('A short summary about the municipality.'))
    country     = CountryField(_('Country'), help_text=_('Select municipality\'s country.'))
    coords      = PointField(_('Coordinates'), blank=False, null=True, help_text=_('Locate the municipality in the map.'))

    class Meta:
        verbose_name        = _('Municipality')
        verbose_name_plural = _('Municipalities')

    def __str__(self):
        """ String representation of this model objects. """
        return self.name or '---'

class Milestone(models.Model):
    """ A milestone is a featured project budgeted by a Municipality """

    name         = models.CharField(_('Name'), max_length=128, blank=False, null=False, help_text=_('Name of the milestone.'))
    description  = models.TextField(_('Summary'), blank=True, help_text=_('A short summary about the milestone.'))
    municipality = models.ForeignKey(Municipality, null=True, verbose_name=_('Municipality'), help_text=_('Select the municipality related to this milestone'))
    year         = models.PositiveIntegerField(_('Year'), help_text=_('Year of this milestone.'))
    budget       = models.PositiveIntegerField(_('Budget'), help_text=_('Budget allocated in this milestone.'))

    def __str__(self):
        """ String representation of this model objects. """
        return self.name

class Dataset(models.Model):
    """ City dataset of a specific year """

    municipality = models.ForeignKey(Municipality, null=True, verbose_name=_('Municipality'), help_text=_('Select the municipality related to this dataset'))
    year         = models.PositiveIntegerField(_('Year'), help_text=_('Year of this dataset.'))
    population   = models.PositiveIntegerField(_('Population'), help_text=_('City population.'))
    source       = models.CharField(_('Source'), max_length=128, null=True, help_text=_('Name of the source of the data provided.'))
    source_link  = models.URLField(_('Source link'), null=True, help_text=_('A link to the source data provided.'))
    # incomes
    in_taxes         = models.PositiveIntegerField(_('Tax revenues'), default=0)
    in_grants        = models.PositiveIntegerField(_('Grants'), default=0)
    in_properties    = models.PositiveIntegerField(_('Property income'), default=0)
    in_fees          = models.PositiveIntegerField(_('Revenues from fees'), default=0)
    in_sales         = models.PositiveIntegerField(_('Revenues from sales of products'), default=0)
    in_penalties     = models.PositiveIntegerField(_('Penalties'), default=0)
    in_nonfinancial  = models.PositiveIntegerField(_('Revenues from sales of non-financial assets'), default=0)
    # expenditures
    ex_wages         = models.PositiveIntegerField(_('Wages'), default=0)
    ex_material      = models.PositiveIntegerField(_('Material costs'), default=0)
    ex_financial     = models.PositiveIntegerField(_('Financial expenses'), default=0)
    ex_subsidies     = models.PositiveIntegerField(_('Subsidies to companies'), default=0)
    ex_grants        = models.PositiveIntegerField(_('Grants'), default=0)
    ex_compensations = models.PositiveIntegerField(_('Compensations'), default=0)
    ex_other         = models.PositiveIntegerField(_('Other expenditures'), default=0)
    ex_nonfinancial  = models.PositiveIntegerField(_('Expenditures for the acquisition of non-financial assets'), default=0)


    def __str__(self):
        """ String representation of this model objects. """
        return self.municipality.name + "#" + self.year or '---'
