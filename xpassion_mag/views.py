import re

from django.http import Http404
from django.utils import text

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_mag.models import Article, ArticleSerializer, Feature, FeatureSerializer, Category, CategorySerializer
from xpassion_mag.models import Issue, IssueSerializer, Theme, ThemeSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('title', 'subtitle', 'author_firstname', 'author_lastname', )

    @decorators.detail_route(methods=['put'])
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_image(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        image = request.data['image']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", image.name) 
        image.name = text.slugify(article.title + " " + article.author_firstname + " " + article.author_lastname) + "." + extension

        if article.image:
            article.image.delete()

        article.image = image
        article.save()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def remove_image(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        article.image.delete()

        serializer = self.get_serializer_class()(article)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_pdf(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404()

        pdf = request.data['pdf']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", pdf.name) 
        if extension not in ["pdf", "PDF"]:
            raise ValueError("this is not a pdf file")
        pdf.name = text.slugify(article.title + " " + article.author_firstname + " " + article.author_lastname) + ".pdf"

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

    @decorators.detail_route(methods=['put'])
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_image(self, request, pk=None):
        try:
            feature = Feature.objects.get(pk=pk)
        except Feature.DoesNotExist:
            raise Http404()

        image = request.data['image']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", image.name) 
        image.name = text.slugify(feature.title) + "." + extension

        if feature.image:
            feature.image.delete()

        feature.image = image
        feature.save()

        serializer = self.get_serializer_class()(feature)
        return Response(serializer.data)

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
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_front(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        front_cover = request.data['front_cover']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", front_cover.name) 
        front_cover.name = text.slugify("{0:0>3}".format(issue.number) + "-front-cover") + "." + extension

        if issue.front_cover:
            issue.front_cover.delete()

        issue.front_cover = front_cover
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
    # @decorators.parser_classes(('MultiPartParser', ))
    def upload_back(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404()

        back_cover = request.data['back_cover']
        extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", back_cover.name) 
        back_cover.name = text.slugify("{0:0>3}".format(issue.number) + "-back-cover") + "." + extension

        if issue.back_cover:
            issue.back_cover.delete()

        issue.back_cover = back_cover
        issue.save()

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
