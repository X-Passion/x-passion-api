from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from xpassion_news.models import News, NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    hit_count = HitCount.objects.get_for_object(News.objects.first())

    def list(self, request):
        HitCountMixin.hit_count(request, self.hit_count)
        return super().list(request)

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
