# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0023_auto_20160416_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['lastname']},
        ),
    ]
