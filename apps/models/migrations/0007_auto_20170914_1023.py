# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_milestone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Municipality name. Use native language.', max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='A short summary about the municipality.', verbose_name='Summary')),
                ('country', django_countries.fields.CountryField(help_text="Select municipality's country.", max_length=2, verbose_name='Country')),
                ('coords', djgeojson.fields.PointField(help_text='Locate the municipality in the map.', null=True, verbose_name='Coordinates')),
            ],
            options={
                'verbose_name_plural': 'Municipalities',
                'verbose_name': 'Municipality',
            },
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='city',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AddField(
            model_name='dataset',
            name='municipality',
            field=models.ForeignKey(help_text='Select the municipality related to this dataset', null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Municipality', verbose_name='Municipality'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='municipality',
            field=models.ForeignKey(help_text='Select the municipality related to this milestone', null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Municipality', verbose_name='Municipality'),
        ),
    ]
