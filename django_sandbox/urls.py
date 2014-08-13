from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_sandbox import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'main.views.index'),
    url(r'^urls/', include('urls_.urls', namespace='urls_')),
    url(r'^models/', include('models_.urls', namespace='models_')),
    url(r'^polls/', include('tutorial_app.urls', namespace='tutorial_app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
