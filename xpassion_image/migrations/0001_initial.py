# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('file', models.ImageField(upload_to='img')),
                ('caption', models.CharField(max_length=254)),
                ('platal_only', models.BooleanField(default=True)),
            ],
        ),
    ]
