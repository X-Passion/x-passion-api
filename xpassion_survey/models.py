from django.db import models
import django.contrib.auth.models
from django import forms
from rest_framework import serializers
from djangojsonschema.jsonschema import DjangoFormToJSONSchema

from collections import OrderedDict

class Survey(models.Model):
    name = models.CharField(max_length=255, unique=True)
    targets = models.ManyToManyField(django.contrib.auth.models.Group)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_targets(self):
        return self.targets

class Page(models.Model):
    survey = models.ForeignKey(
            Survey,
            on_delete=models.CASCADE
            )
    rank = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255, blank=True)
    #form_objects = FormPageManager()
    
    def __str__(self):
        return str(self.survey) +' - '+ str(self.rank) +' '+ self.name
    def get_targets(self):
        return self.survey.get_targets()


class Question(models.Model):
    OPEN    = 'O'
    BOOLEAN = 'B'
    MCQ     = 'M'
    EMCQ    = 'E'
    SCALE   = 'S'
    
    QTYPE = (
            (OPEN,      'Open'),
            (BOOLEAN,   'Boolean (yes/no)'),
            (MCQ,       'Multiple choice, non-exclusive'),
            (EMCQ,      'Multiple choice, exclusive'),
            (SCALE,     'Scale'),
            )
    page = models.ForeignKey(
            Page,
            on_delete=models.CASCADE
            )
    rank = models.PositiveSmallIntegerField()
    wording = models.CharField(max_length=255)
    qtype = models.CharField(max_length=1, choices=QTYPE)
    hint = models.CharField(max_length=255, blank=True)
    scale_max = models.PositiveSmallIntegerField(blank=True, null=True)
    auto_other_choice = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "%s %d.%d" % (self.page.survey, self.page.rank, self.rank)
    def get_targets(self):
        return self.page.get_targets()

class Choice(models.Model):
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE
            )
    rank = models.PositiveSmallIntegerField()
    wording = models.CharField(max_length=255)
    open_choice = models.BooleanField(default=False)
    hint = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return "%s - %d : %s" % (self.question, self.rank, self.wording)
    def get_targets(self):
        return self.question.get_targets()

## Typed django form for a Page
class PageForm(forms.Form):
    ## Behave like a model
    #objects = Page.form_objects
    
    def __init__(self, page):
        super().__init__()
        for question in page.question_set.all():
            if question.qtype == Question.OPEN:
                self.fields[str(question.rank)] = forms.CharField(
                        label=question.wording,
                        help_text=question.hint
                        )
            elif question.qtype == Question.EMCQ:
                self.fields[str(question.rank)] = forms.ChoiceField(
                        label=question.wording,
                        choices= [ (c.pk, c.wording) for c in
                            question.choice_set.all() ],
                        widget=forms.RadioSelect
                        )
                
           # TODO : add other types once it works

#PageForm.objects.to_model = PageForm

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('name','page_set')

class PageFormSerializer(serializers.Serializer):
    def to_representation(self, instance):
        form = PageForm(instance)
        return DjangoFormToJSONSchema().convert_form(form)
