from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=254)
    message = models.TextField()
    # image = models.ImageField(upload_to="img/news", blank=True, null=True)
    author = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title + self.date.strftime(" (%d/%m/%Y %H:%M)")

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News

    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())