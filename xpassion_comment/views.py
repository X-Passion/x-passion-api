from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from xpassion_comment.models import Comment, CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404()

        comment.deleted = True
        comment.save()

        serializer = self.get_serializer_class()(comment)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404()

        comment.deleted = False
        comment.save()

        serializer = self.get_serializer_class()(comment)
        return Response(serializer.data)