import re

from django.http import Http404
from django.utils import text

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_news.models import News, NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404()

        news.deleted = True
        news.save()

        serializer = self.get_serializer_class()(news, context={'request': request})
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404()

        news.deleted = False
        news.save()

        serializer = self.get_serializer_class()(news, context={'request': request})
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_image(self, request, pk=None):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404()

        image = request.data['image']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", image.name) 
        image.name = text.slugify(news.date.strftime("%Y%m%d%H%M") + " " + news.title) + "." + extension

        if news.image:
            news.image.delete()

        news.image = image
        news.save()

        serializer = self.get_serializer_class()(news)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def remove_image(self, request, pk=None):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404()

        news.image.delete()

        serializer = self.get_serializer_class()(news)
        return Response(serializer.data)