import datetime

from django.db import models

from rest_framework import serializers


class Image(models.Model):
    file = models.ImageField(upload_to='img')
    caption = models.CharField(max_length=254)
    platal_only = models.BooleanField(default=True)

    def __str__(self):
        return self.file.name


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image