# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=254)),
                ('intro_paragraph', models.TextField(blank=True)),
                ('color', models.CharField(max_length=10)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
