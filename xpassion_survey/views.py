from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.exceptions import ValidationError
from django.http import Http404

from . import models
from .permissions import IsSurveyTarget

class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    # TODO : add filter
    queryset = models.Survey.objects.all()
    serializer_class = models.SurveySerializer
    permission_classes = [IsSurveyTarget]

    def get_queryset(self):
        return super().get_queryset().filter(active=True)
    
    @action(detail=False)
    def current(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            survey = queryset.first()
            if survey is None:
                raise Http404
            self.check_object_permissions(request, survey)
            serializer = self.get_serializer(survey)
            return Response(serializer.data)

        except (TypeError, ValueError, ValidationError):
            raise Http404


class PageFormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Page.objects.all()
    serializer_class = models.PageFormSerializer
    permission_classes = [IsSurveyTarget]
