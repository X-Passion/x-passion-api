from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_image.models import Image, ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_fields = ['type']
