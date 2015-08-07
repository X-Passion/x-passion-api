# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0011_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/articles', null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/features', null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='back_cover',
            field=models.ImageField(blank=True, upload_to='img/covers', null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='front_cover',
            field=models.ImageField(blank=True, upload_to='img/covers', null=True),
        ),
    ]
