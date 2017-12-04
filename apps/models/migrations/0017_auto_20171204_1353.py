# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0016_cofoglevel_datasetitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasetitem',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetitem',
            name='level',
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_1',
            field=models.PositiveIntegerField(null=True, verbose_name='Executive and legislative organs, financial and fiscal affairs, external affairs'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_10',
            field=models.PositiveIntegerField(null=True, verbose_name='Civil defence'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_11',
            field=models.PositiveIntegerField(null=True, verbose_name='Foreign military aid'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_12',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D defence'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_13',
            field=models.PositiveIntegerField(null=True, verbose_name='Defence (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_14',
            field=models.PositiveIntegerField(null=True, verbose_name='Police services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_15',
            field=models.PositiveIntegerField(null=True, verbose_name='Fire-protection services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_16',
            field=models.PositiveIntegerField(null=True, verbose_name='Law courts'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_17',
            field=models.PositiveIntegerField(null=True, verbose_name='Prisons'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_18',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D public order and safety'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_19',
            field=models.PositiveIntegerField(null=True, verbose_name='Public order and safety (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_2',
            field=models.PositiveIntegerField(null=True, verbose_name='Foreign economic aid'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_20',
            field=models.PositiveIntegerField(null=True, verbose_name='General economic, commercial and labour affairs'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_21',
            field=models.PositiveIntegerField(null=True, verbose_name='Agriculture, forestry, fishing and hunting'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_22',
            field=models.PositiveIntegerField(null=True, verbose_name='Fuel and energy'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_23',
            field=models.PositiveIntegerField(null=True, verbose_name='Mining, manufacturing and construction'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_24',
            field=models.PositiveIntegerField(null=True, verbose_name='Transport'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_25',
            field=models.PositiveIntegerField(null=True, verbose_name='Communication'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_26',
            field=models.PositiveIntegerField(null=True, verbose_name='Other industries'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_27',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D economic affairs'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_28',
            field=models.PositiveIntegerField(null=True, verbose_name='Economic affairs (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_29',
            field=models.PositiveIntegerField(null=True, verbose_name='Waste management'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_3',
            field=models.PositiveIntegerField(null=True, verbose_name='General services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_30',
            field=models.PositiveIntegerField(null=True, verbose_name='Waste water management'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_32',
            field=models.PositiveIntegerField(null=True, verbose_name='Pollution abatement'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_33',
            field=models.PositiveIntegerField(null=True, verbose_name='Protection of biodiversity and landscape'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_34',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D environmental protection'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_35',
            field=models.PositiveIntegerField(null=True, verbose_name='Environmental protection (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_36',
            field=models.PositiveIntegerField(null=True, verbose_name='Housing development'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_37',
            field=models.PositiveIntegerField(null=True, verbose_name='Community development'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_38',
            field=models.PositiveIntegerField(null=True, verbose_name='Water supply'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_39',
            field=models.PositiveIntegerField(null=True, verbose_name='Street lighting'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_4',
            field=models.PositiveIntegerField(null=True, verbose_name='Basic research'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_40',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D housing and community amenities'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_42',
            field=models.PositiveIntegerField(null=True, verbose_name='Housing and community amenities (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_43',
            field=models.PositiveIntegerField(null=True, verbose_name='Medical products, appliances and equipment'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_44',
            field=models.PositiveIntegerField(null=True, verbose_name='Outpatient services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_45',
            field=models.PositiveIntegerField(null=True, verbose_name='Hospital services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_46',
            field=models.PositiveIntegerField(null=True, verbose_name='Public health services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_47',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D health'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_48',
            field=models.PositiveIntegerField(null=True, verbose_name='Health (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_49',
            field=models.PositiveIntegerField(null=True, verbose_name='Recreational and sporting services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_5',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D general public services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_50',
            field=models.PositiveIntegerField(null=True, verbose_name='Cultural services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_51',
            field=models.PositiveIntegerField(null=True, verbose_name='Broadcasting and publishing services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_52',
            field=models.PositiveIntegerField(null=True, verbose_name='Religious and other community services'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_53',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D recreation, culture and religion'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_54',
            field=models.PositiveIntegerField(null=True, verbose_name='Recreation, culture and religion (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_55',
            field=models.PositiveIntegerField(null=True, verbose_name='Pre-primary and primary education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_56',
            field=models.PositiveIntegerField(null=True, verbose_name='Secondary education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_57',
            field=models.PositiveIntegerField(null=True, verbose_name='Post-secondary non-tertiary education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_58',
            field=models.PositiveIntegerField(null=True, verbose_name='Tertiary education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_59',
            field=models.PositiveIntegerField(null=True, verbose_name='Education not definable by level'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_6',
            field=models.PositiveIntegerField(null=True, verbose_name='General public services n.e.c'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_60',
            field=models.PositiveIntegerField(null=True, verbose_name='Subsidiary services to education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_61',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D education'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_62',
            field=models.PositiveIntegerField(null=True, verbose_name='Education (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_63',
            field=models.PositiveIntegerField(null=True, verbose_name='Sickness and disability'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_64',
            field=models.PositiveIntegerField(null=True, verbose_name='Old age'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_65',
            field=models.PositiveIntegerField(null=True, verbose_name='Survivors'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_66',
            field=models.PositiveIntegerField(null=True, verbose_name='Family and children'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_67',
            field=models.PositiveIntegerField(null=True, verbose_name='Unemployment'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_68',
            field=models.PositiveIntegerField(null=True, verbose_name='Housing'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_69',
            field=models.PositiveIntegerField(null=True, verbose_name='Social exclusion (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_7',
            field=models.PositiveIntegerField(null=True, verbose_name='Public debt transactions'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_70',
            field=models.PositiveIntegerField(null=True, verbose_name='R&D social protection'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_71',
            field=models.PositiveIntegerField(null=True, verbose_name='Social protection (not classified)'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_8',
            field=models.PositiveIntegerField(null=True, verbose_name='Transfers of a general character between different levels of government'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='concept_9',
            field=models.PositiveIntegerField(null=True, verbose_name='Military defence'),
        ),
        migrations.DeleteModel(
            name='CofogLevel',
        ),
        migrations.DeleteModel(
            name='DatasetItem',
        ),
    ]
