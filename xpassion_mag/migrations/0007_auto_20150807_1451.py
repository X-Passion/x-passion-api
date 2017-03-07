# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0006_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='deleted',
        ),
    ]
