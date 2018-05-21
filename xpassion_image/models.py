import datetime

from django.db import models
from django.utils import text

from rest_framework import serializers

from image_cropping import ImageRatioField

def target_folder(instance, filename):
    path = 'img/' + instance.type + '/'
    if instance.caption:
        path = path + text.slugify(instance.caption)
    return path


class ImageManager(models.Manager):
    def create_image(self, file, caption='', platal_only=True, type='covers'):
        image = self.create(file=file, caption=caption, platal_only=platal_only, type=type)
        return image


class Image(models.Model):
    IMAGE_TYPES = [
        ('news', 'News'),
        ('covers', 'Cover'),
        ('features', 'Feature'),
        ('articles', 'Article')
    ]

    file = models.ImageField(upload_to=target_folder, max_length=254)
    caption = models.CharField(max_length=254)
    subcaption = models.CharField(max_length=254, blank=True, null=True)
    platal_only = models.BooleanField(default=True)
    type = models.CharField(max_length=10, choices=IMAGE_TYPES, default='covers')
    big_cropping = ImageRatioField('file', '829x1168')
    small_cropping = ImageRatioField('file', '282x400')

    objects = ImageManager

    def __str__(self):
        return self.file.name


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
