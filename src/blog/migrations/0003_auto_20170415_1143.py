# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-15 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170415_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageCarouselItem',
        ),
    ]
