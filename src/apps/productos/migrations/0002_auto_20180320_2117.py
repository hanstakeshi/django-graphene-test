# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='codigo',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='nombre',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Nombre'),
        ),
    ]
