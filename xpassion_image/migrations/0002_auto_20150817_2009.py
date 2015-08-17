# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.CharField(max_length=10, default='covers', choices=[('news', 'News'), ('covers', 'Cover'), ('features', 'Feature'), ('articles', 'Article')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(max_length=254, upload_to='target_folder'),
        ),
    ]
