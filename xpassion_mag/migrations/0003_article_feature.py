# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0002_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='feature',
            field=models.ForeignKey(blank=True, to='xpassion_mag.Feature', null=True),
        ),
    ]
