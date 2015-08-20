import re

from django.http import Http404
from django.utils import text
from django.db.models import Prefetch

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_mag.models import Article, ArticleSerializer, Feature, FeatureSerializer, Category, CategorySerializer, Issue, IssueSerializer
from xpassion_image.models import ImageSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('title', 'subtitle', 'author_firstname', 'author_lastname', )

    @decorators.detail_route(methods=['put'])
    def upload_pdf(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        pdf = request.data['pdf']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", pdf.name) 
        if extension not in ["pdf", "PDF"]:
            raise ValueError("this is not a pdf file")
        pdf.name = text.slugify(article.author_lastname + " " + article.author_firstname + " " + article.title) + ".pdf"

        if article.pdf:
            article.pdf.delete()

        article.pdf = pdf
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def remove_pdf(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.pdf.delete()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    search_fields = ('title', )


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def retrieve(self, request, pk=None):
        try:
            qs = Issue.objects.select_related('front_cover')
            qs = qs.prefetch_related(
                Prefetch('features', queryset=Feature.objects.select_related('image')),
                Prefetch('articles', queryset=Article.objects.select_related('image', 'category')),
            )
            issue = qs.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        serializer = self.get_serializer_class()(issue, context={'request': request})
        return Response(serializer.data)
        

    @decorators.detail_route(methods=['put'])
    def unpublish(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.published = False
        issue.save()

        serializer = self.get_serializer_class()(issue, context={'request': request})
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def publish(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        issue.published = True
        issue.save()

        serializer = self.get_serializer_class()(issue, context={'request': request})
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
