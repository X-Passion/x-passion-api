# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0021_article_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lastname', models.CharField(max_length=254)),
                ('firstname', models.CharField(max_length=254)),
                ('promotion', models.IntegerField(null=True, default=2014, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author_firstname',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author_lastname',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author_promotion',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='xpassion_mag.Author', related_name='articles', default=None),
        ),
    ]
