# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_image', '0003_auto_20150817_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='subcaption',
            field=models.CharField(null=True, max_length=254, blank=True),
        ),
    ]
