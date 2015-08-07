from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_mag.models import Article, ArticleSerializer, Feature, FeatureSerializer, Category, CategorySerializer
from xpassion_mag.models import Issue, IssueSerializer, Theme, ThemeSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('title', 'subtitle', 'author_firstname', 'author_lastname', )

    @decorators.detail_route(methods=['put'])
    def remove_image(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.image.delete()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    search_fields = ('title', )

    @decorators.detail_route(methods=['put'])
    def remove_image(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        feature.image.delete()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    @decorators.detail_route(methods=['put'])
    def unpublish(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.published = False
        issue.save()

        serializer = self.get_serializer_class()(issue)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def publish(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.published = True
        issue.save()

        serializer = self.get_serializer_class()(issue)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def remove_front(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.front_cover.delete()

        serializer = self.get_serializer_class()(issue)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def remove_back(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.back_cover.delete()

        serializer = self.get_serializer_class()(issue)
        return Response(serializer.data)


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
