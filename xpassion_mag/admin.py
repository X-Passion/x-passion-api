from django.contrib import admin
from django.contrib.auth.models import Group
from xpassion_mag.models import Article, Feature, Issue, Category

admin.site.unregister(Group)

admin.site.register(Article)
admin.site.register(Feature)
admin.site.register(Issue)
admin.site.register(Category)