# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0008_auto_20150807_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='number',
            field=models.IntegerField(unique=True, default=0),
        ),
    ]
