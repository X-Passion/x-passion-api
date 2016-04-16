# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0018_auto_20150820_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_promotion',
            field=models.IntegerField(null=True, blank=True, default=2014),
        ),
    ]
