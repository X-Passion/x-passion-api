#-*- coding: utf-8 -*-
import datetime

from django.db import models

from rest_framework import serializers

from xpassion_image.models import Image, ImageSerializer


class Issue(models.Model):
    """An issue published by the 'binet'"""
    date = models.DateField()
    theme = models.CharField(max_length=254)
    published = models.BooleanField(default=False)
    front_cover = models.ForeignKey(Image, blank=True, null=True)
    number = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return "Numéro {nb} paru le ".format(nb=self.number) + self.date.strftime("%d/%m/%Y") + " : {theme}".format(theme=self.theme)


class Category(models.Model):
    """Category for Articles"""
    name = models.CharField(max_length=254, unique=True)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Feature(models.Model):
    """A group of articles dealing with the same topic"""
    title = models.CharField(max_length=254)
    intro_paragraph = models.TextField(blank=True)
    image = models.ForeignKey(Image, blank=True, null=True)
    issue = models.ForeignKey(Issue, related_name="features")
    color = models.CharField(max_length=10, default="#ffffff")

    def __str__(self):
        return self.title


class Author(models.Model):
    """Authors of articles"""
    class Meta:
        ordering = ['lastname']

    lastname = models.CharField(max_length=254)
    firstname = models.CharField(max_length=254)
    promotion = models.IntegerField(default=2014, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Article(models.Model):
    """An article published in an Issue"""
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="articles", blank=True)
    description = models.CharField(max_length=254, default="")
    intro_paragraph = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    begin_page = models.IntegerField(default=0)
    end_page = models.IntegerField(default=0)
    pdf = models.FileField(upload_to="pdf", blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True)
    feature = models.ForeignKey(Feature, blank=True, null=True)
    issue = models.ForeignKey(Issue, related_name="articles")
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def is_visible(self):
        return self.issue.published


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature

    image = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), allow_null=True)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article


    visible = serializers.BooleanField(source='is_visible', read_only=True)
    #image = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), allow_null=True)
    image = ImageSerializer(read_only=True, allow_null=True)
    authors = AuthorSerializer(read_only=True, many=True)
    #image = serializers.HyperlinkedRelatedField(queryset=Image.objects.all(), allow_null=True, view_name="")
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def validate(self, data):
        if data['begin_page'] > data['end_page']:
            raise serializers.ValidationError("end page must be greater or equal begin page")
        return data

    def create(self, validated_data):
        validated_data['category'] = Category.objects.get(pk=1)
        validated_data.pop("category_id", None)
        return Article.objects.create(**validated_data)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        read_only_fields = ('published', )
        depth = 1

    articles = ArticleSerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
