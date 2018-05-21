# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0004_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(to='xpassion_mag.Issue',
                on_delete=models.CASCADE, default=1),
            preserve_default=False,
        ),
    ]
