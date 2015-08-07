from django.db import models

from rest_framework import serializers


class Issue(models.Model):
    """An issue published by the 'binet'"""
    date = models.DateField()
    published = models.BooleanField(default=True)
    # front_cover = models.ImageField(upload_to="covers", blank=True, null=True)
    # back_cover = models.ImageField(upload_to="covers", blank=True, null=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return "Numéro {nb} paru le {date}".format(nb=self.number, date=self.date)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue


class Feature(models.Model):
    """A group of articles dealing with the same topic"""
    title = models.CharField(max_length=254)
    intro_paragraph = models.TextField(blank=True)
    color = models.CharField(max_length=10)
    # image = models.ImageField(upload_to="img", blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature


class Article(models.Model):
    """An article published in an Issue"""
    title = models.CharField(max_length=254)
    author_lastname = models.CharField(max_length=254)
    author_firstname = models.CharField(max_length=254)
    subtitle = models.TextField(blank=True)
    intro_paragraph = models.TextField(blank=True)
    begin_page = models.IntegerField(default=0)
    end_page = models.IntegerField(default=0)
    # pdf = models.FileField(upload_to="pdf", blank=True, null=True)
    color = models.CharField(max_length=10)
    # image = models.ImageField(upload_to="img", blank=True, null=True)
    feature = models.ForeignKey(Feature, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

    def validate(self, data):
        if data['begin_page'] > data['end_page']:
            raise serializers.ValidationError("end page must be greater or equal begin page")
        return data
