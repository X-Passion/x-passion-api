# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0007_auto_20150807_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
