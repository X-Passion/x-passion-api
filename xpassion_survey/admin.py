import django.contrib.admin

from . import models

django.contrib.admin.site.register([
    models.Survey,
    models.Page,
    models.Question,
    models.Choice,
    ])

