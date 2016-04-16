# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0027_auto_20160416_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='color',
            field=models.CharField(max_length=10, default='#ffffff'),
        ),
    ]
