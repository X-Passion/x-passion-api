# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0012_auto_20150807_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf', blank=True),
        ),
    ]
