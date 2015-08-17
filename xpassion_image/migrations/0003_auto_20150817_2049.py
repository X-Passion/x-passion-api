# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import xpassion_image.models


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_image', '0002_auto_20150817_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(max_length=254, upload_to=xpassion_image.models.target_folder),
        ),
    ]
