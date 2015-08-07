import datetime

from django.db import models
from django.utils import timezone
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response


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


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('title', 'subtitle', 'author_firstname', 'author_lastname', )

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.deleted = True
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.deleted = False
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)
