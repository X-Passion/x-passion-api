import datetime

from django.db import models
from django.utils import timezone
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response


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


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    search_fields = ('title', )

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        feature.deleted = True
        feature.save()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        feature.deleted = False
        feature.save()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)
