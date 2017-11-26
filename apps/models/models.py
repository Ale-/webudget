# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# contrib
from djgeojson.fields import PointField
from django_countries.fields import CountryField
from ckeditor_uploader.fields import RichTextUploadingField
# apps
from . import validators, utils

validate_image_size = validators.ImageSizeValidator({ 'min_width' : 600, 'min_height' : 300, 'max_width' : 1920, 'max_height' : 1280 })
validate_image_type = validators.ImageTypeValidator(["jpeg", "png"])
city_images_path  = utils.RenameImage("images/cities/")

class Municipality(models.Model):
    """ Municipality """

    name        = models.CharField(_('Name'), max_length=128, blank=False, null=False, help_text=_('Municipality name. Use native language.'))
    slug        = models.SlugField(editable=False, default="---")
    description = models.TextField(_('Summary'), blank=True, help_text=_('A short summary about the municipality.'))
    country     = CountryField(_('Country'), help_text=_('Select municipality\'s country.'))
    coords      = PointField(_('Coordinates'), blank=False, null=True, help_text=_('Locate the municipality in the map.'))
    image       = models.ImageField(_('Image'), blank=True, null=True, validators=[validate_image_size, validate_image_type],
                                    upload_to = city_images_path,
                                    help_text=_('Representative image of the municipality for the views.') )

    class Meta:
        verbose_name        = _('Municipality basic data')
        verbose_name_plural = _('Municipalities basic data')

    def __str__(self):
        """ String representation of this model objects. """
        return self.name or '---'

    def save(self, *args, **kwargs):
        """ Update city slug when updating content """
        self.slug = slugify(self.name)
        super(Municipality, self).save(*args, **kwargs)

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

    class Meta:
        verbose_name        = _('Municipality milestone')
        verbose_name_plural = _('Municipalities milestones')

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

    class Meta:
        verbose_name        = _('Municipality dataset')
        verbose_name_plural = _('Municipalities datasets')

class Block(models.Model):
    """ Text blocks """

    title         = models.CharField(_('Title'), max_length=128, blank=False, null=False, help_text=_('Title of the block.'))
    body          = RichTextUploadingField(_('Summary'), blank=True, help_text=_('Text body of the block'))

    def __str__(self):
        """ String representation of this model objects. """
        return self.title

    class Meta:
        verbose_name        = _('Text block')
        verbose_name_plural = _('Text blocks')
