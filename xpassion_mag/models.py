import datetime

from django.db import models

from rest_framework import serializers


class Issue(models.Model):
    """An issue published by the 'binet'"""
    date = models.DateField()
    published = models.BooleanField(default=False)
    front_cover = models.ImageField(upload_to="img/covers", blank=True, null=True)
    back_cover = models.ImageField(upload_to="img/covers", blank=True, null=True)
    number = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return "Numéro {nb} paru le ".format(nb=self.number) + self.date.strftime("%d/%m/%Y")

    def save(self, *args, **kwargs):
        add_front = False
        if self.front_cover:
            if not self.pk:
                add_front = True
            else:
                orig = Issue.objects.get(pk=self.pk)
                if orig.front_cover != self.front_cover:
                    orig.front_cover.delete()
                    add_front = True
        else:
            if self.pk:
                orig = Issue.objects.get(pk=self.pk)
                self.front_cover = orig.front_cover

        if add_front:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.front_cover.name) 
            self.front_cover.name = text.slugify(self.title) + "." + extension

        add_back = False
        if self.back_cover:
            if not self.pk:
                add_back = True
            else:
                orig = Issue.objects.get(pk=self.pk)
                if orig.back_cover != self.back_cover:
                    orig.back_cover.delete()
                    add_back = True
        else:
            if self.pk:
                orig = Issue.objects.get(pk=self.pk)
                self.back_cover = orig.back_cover

        if add_back:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.back_cover.name) 
            self.back_cover.name = text.slugify(self.title) + "." + extension

        super(Issue, self).save(*args, **kwargs)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        read_only_fields = ('published', )


class Theme(models.Model):
    """Theme for Issues"""
    name = models.CharField(max_length=254)
    issue = models.ForeignKey(Issue)

    def __str__(self):
        return self.name


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme


class Category(models.Model):
    """Category for Articles"""
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
    

class Feature(models.Model):
    """A group of articles dealing with the same topic"""
    title = models.CharField(max_length=254)
    intro_paragraph = models.TextField(blank=True)
    color = models.CharField(max_length=10)
    image = models.ImageField(upload_to="img/features", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        add_image = False
        if self.image:
            if not self.pk:
                add_image = True
            else:
                orig = Feature.objects.get(pk=self.pk)
                if orig.image != self.image:
                    orig.image.delete()
                    add_image = True
        else:
            if self.pk:
                orig = Feature.objects.get(pk=self.pk)
                self.image = orig.image

        if add_image:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.image.name) 
            self.image.name = text.slugify(self.title) + "." + extension

        super(Feature, self).save(*args, **kwargs)


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
    image = models.ImageField(upload_to="img/articles", blank=True, null=True)
    feature = models.ForeignKey(Feature, blank=True, null=True)
    issue = models.ForeignKey(Issue)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def is_visible(self):
        return self.issue.published

    def save(self, *args, **kwargs):
        add_image = False
        if self.image:
            if not self.pk:
                add_image = True
            else:
                orig = Article.objects.get(pk=self.pk)
                if orig.image != self.image:
                    orig.image.delete()
                    add_image = True
        else:
            if self.pk:
                orig = Article.objects.get(pk=self.pk)
                self.image = orig.image

        if add_image:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.image.name) 
            self.image.name = text.slugify(self.title + "-" + self.issue.id) + "." + extension

        super(Article, self).save(*args, **kwargs)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

    visible = serializers.BooleanField(source='is_visible', read_only=True)

    def validate(self, data):
        if data['begin_page'] > data['end_page']:
            raise serializers.ValidationError("end page must be greater or equal begin page")
        return data
