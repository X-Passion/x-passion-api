from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from xpassion_mag.views import ArticleViewSet, FeatureViewSet, IssueViewSet, ThemeViewSet, CategoryViewSet
from xpassion_news.views import NewsViewSet
from xpassion_comment.views import CommentViewSet

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^', include(router.urls))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()