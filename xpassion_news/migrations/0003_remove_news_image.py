# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_news', '0002_auto_20150807_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
