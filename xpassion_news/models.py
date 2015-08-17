from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers

from xpassion_image.models import Image, ImageSerializer


class News(models.Model):
    class Meta:
        verbose_name_plural = "News"
    
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=254)
    message = models.TextField()
    image = models.ForeignKey(Image, blank=True, null=True)
    author = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title + self.date.strftime(" (%d/%m/%Y %H:%M)")


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News

    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    image = ImageSerializer()
