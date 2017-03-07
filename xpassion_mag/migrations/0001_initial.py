# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=254)),
                ('author_lastname', models.CharField(max_length=254)),
                ('author_firstname', models.CharField(max_length=254)),
                ('subtitle', models.TextField(blank=True)),
                ('intro_paragraph', models.TextField(blank=True)),
                ('begin_page', models.IntegerField(default=0)),
                ('end_page', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=10)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
