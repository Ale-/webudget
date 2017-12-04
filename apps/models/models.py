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
    concept_ps_1 = models.PositiveIntegerField(_('Executive and legislative organs, financial and fiscal affairs, external affairs'), null=True)
    concept_ps_2 = models.PositiveIntegerField(_('Foreign economic aid'), null=True)
    concept_ps_3 = models.PositiveIntegerField(_('General services'), null=True)
    concept_ps_4 = models.PositiveIntegerField(_('Basic research'), null=True)
    concept_ps_5 = models.PositiveIntegerField(_('R&D general public services'), null=True)
    concept_ps_6 = models.PositiveIntegerField(_('General public services n.e.c'), null=True)
    concept_ps_7 = models.PositiveIntegerField(_('Public debt transactions'), null=True)
    concept_ps_8 = models.PositiveIntegerField(_('Transfers of a general character between different levels of government'), null=True)
    concept_de_1 = models.PositiveIntegerField(_('Military defence'), null=True)
    concept_de_2 = models.PositiveIntegerField(_('Civil defence'), null=True)
    concept_de_3 = models.PositiveIntegerField(_('Foreign military aid'), null=True)
    concept_de_4 = models.PositiveIntegerField(_('R&D defence'), null=True)
    concept_de_5 = models.PositiveIntegerField(_('Defence (not classified)'), null=True)
    concept_po_1 = models.PositiveIntegerField(_('Police services'), null=True)
    concept_po_2 = models.PositiveIntegerField(_('Fire-protection services'), null=True)
    concept_po_3 = models.PositiveIntegerField(_('Law courts'), null=True)
    concept_po_4 = models.PositiveIntegerField(_('Prisons'), null=True)
    concept_po_5 = models.PositiveIntegerField(_('R&D public order and safety'), null=True)
    concept_po_6 = models.PositiveIntegerField(_('Public order and safety (not classified)'), null=True)
    concept_ea_1 = models.PositiveIntegerField(_('General economic, commercial and labour affairs'), null=True)
    concept_ea_2 = models.PositiveIntegerField(_('Agriculture, forestry, fishing and hunting'), null=True)
    concept_ea_3 = models.PositiveIntegerField(_('Fuel and energy'), null=True)
    concept_ea_4 = models.PositiveIntegerField(_('Mining, manufacturing and construction'), null=True)
    concept_ea_5 = models.PositiveIntegerField(_('Transport'), null=True)
    concept_ea_6 = models.PositiveIntegerField(_('Communication'), null=True)
    concept_ea_7 = models.PositiveIntegerField(_('Other industries'), null=True)
    concept_ea_8 = models.PositiveIntegerField(_('R&D economic affairs'), null=True)
    concept_ea_9 = models.PositiveIntegerField(_('Economic affairs (not classified)'), null=True)
    concept_ep_1 = models.PositiveIntegerField(_('Waste management'), null=True)
    concept_ep_2 = models.PositiveIntegerField(_('Waste water management'), null=True)
    concept_ep_3 = models.PositiveIntegerField(_('Pollution abatement'), null=True)
    concept_ep_4 = models.PositiveIntegerField(_('Protection of biodiversity and landscape'), null=True)
    concept_ep_5 = models.PositiveIntegerField(_('R&D environmental protection'), null=True)
    concept_ep_6 = models.PositiveIntegerField(_('Environmental protection (not classified)'), null=True)
    concept_ho_1 = models.PositiveIntegerField(_('Housing development'), null=True)
    concept_ho_2 = models.PositiveIntegerField(_('Community development'), null=True)
    concept_ho_3 = models.PositiveIntegerField(_('Water supply'), null=True)
    concept_ho_4 = models.PositiveIntegerField(_('Street lighting'), null=True)
    concept_ho_5 = models.PositiveIntegerField(_('R&D housing and community amenities'), null=True)
    concept_ho_6 = models.PositiveIntegerField(_('Housing and community amenities (not classified)'), null=True)
    concept_he_1 = models.PositiveIntegerField(_('Medical products, appliances and equipment'), null=True)
    concept_he_2 = models.PositiveIntegerField(_('Outpatient services'), null=True)
    concept_he_3 = models.PositiveIntegerField(_('Hospital services'), null=True)
    concept_he_4 = models.PositiveIntegerField(_('Public health services'), null=True)
    concept_he_5 = models.PositiveIntegerField(_('R&D health'), null=True)
    concept_he_6 = models.PositiveIntegerField(_('Health (not classified)'), null=True)
    concept_re_1 = models.PositiveIntegerField(_('Recreational and sporting services'), null=True)
    concept_re_2 = models.PositiveIntegerField(_('Cultural services'), null=True)
    concept_re_3 = models.PositiveIntegerField(_('Broadcasting and publishing services'), null=True)
    concept_re_4 = models.PositiveIntegerField(_('Religious and other community services'), null=True)
    concept_re_5 = models.PositiveIntegerField(_('R&D recreation, culture and religion'), null=True)
    concept_re_6 = models.PositiveIntegerField(_('Recreation, culture and religion (not classified)'), null=True)
    concept_ed_1 = models.PositiveIntegerField(_('Pre-primary and primary education'), null=True)
    concept_ed_2 = models.PositiveIntegerField(_('Secondary education'), null=True)
    concept_ed_3 = models.PositiveIntegerField(_('Post-secondary non-tertiary education'), null=True)
    concept_ed_4 = models.PositiveIntegerField(_('Tertiary education'), null=True)
    concept_ed_5 = models.PositiveIntegerField(_('Education not definable by level'), null=True)
    concept_ed_6 = models.PositiveIntegerField(_('Subsidiary services to education'), null=True)
    concept_ed_7 = models.PositiveIntegerField(_('R&D education'), null=True)
    concept_ed_8 = models.PositiveIntegerField(_('Education (not classified)'), null=True)
    concept_so_1 = models.PositiveIntegerField(_('Sickness and disability'), null=True)
    concept_so_2 = models.PositiveIntegerField(_('Old age'), null=True)
    concept_so_3 = models.PositiveIntegerField(_('Survivors'), null=True)
    concept_so_4 = models.PositiveIntegerField(_('Family and children'), null=True)
    concept_so_5 = models.PositiveIntegerField(_('Unemployment'), null=True)
    concept_so_6 = models.PositiveIntegerField(_('Housing'), null=True)
    concept_so_7 = models.PositiveIntegerField(_('Social exclusion (not classified)'), null=True)
    concept_so_8 = models.PositiveIntegerField(_('R&D social protection'), null=True)
    concept_so_9 = models.PositiveIntegerField(_('Social protection (not classified)'), null=True)


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
