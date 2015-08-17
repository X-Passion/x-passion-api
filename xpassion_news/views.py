from django.http import Http404

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
