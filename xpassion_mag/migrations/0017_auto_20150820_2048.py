# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0016_auto_20150817_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='subtitle',
            new_name='excerpt',
        ),
        migrations.AddField(
            model_name='feature',
            name='issue',
            field=models.ForeignKey(related_name='features', to='xpassion_mag.Issue', default=1),
            preserve_default=False,
        ),
    ]
