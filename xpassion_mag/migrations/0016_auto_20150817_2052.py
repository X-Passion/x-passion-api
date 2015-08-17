# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_image', '0003_auto_20150817_2049'),
        ('xpassion_mag', '0015_auto_20150817_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(null=True, to='xpassion_image.Image', blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ForeignKey(null=True, to='xpassion_image.Image', blank=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='front_cover',
            field=models.ForeignKey(null=True, to='xpassion_image.Image', blank=True),
        ),
    ]
