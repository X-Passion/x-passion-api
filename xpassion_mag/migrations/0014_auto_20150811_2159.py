# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpassion_mag', '0013_article_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='issue',
        ),
        migrations.AddField(
            model_name='issue',
            name='theme',
            field=models.CharField(default='Musique et Russie', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(to='xpassion_mag.Issue',
                on_delete=models.CASCADE, related_name='articles'),
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]
