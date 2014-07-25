from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'main.views.index'),
    url(r'^urls/', include('django_url_test.urls', namespace='django_url_test')),
    url(r'^models/', include('django_models_test.urls', namespace='django_models_test')),
    url(r'^polls/', include('django_tutorial_app.urls', namespace='django_tutorial_app')),
    url(r'^admin/', include(admin.site.urls)),
)
