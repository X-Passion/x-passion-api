# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0014_auto_20150811_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='color',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='color',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='image',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='back_cover',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='front_cover',
        ),
    ]
