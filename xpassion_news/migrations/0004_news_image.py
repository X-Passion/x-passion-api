# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_image', '0001_initial'),
        ('xpassion_news', '0003_remove_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ForeignKey(blank=True, to='xpassion_image.Image', null=True),
        ),
    ]
