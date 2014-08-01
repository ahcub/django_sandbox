from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_sandbox import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'main.views.index'),
    url(r'^urls/', include('django_url_test.urls', namespace='django_url_test')),
    url(r'^models/', include('django_models_test.urls', namespace='django_models_test')),
    url(r'^polls/', include('django_tutorial_app.urls', namespace='django_tutorial_app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
