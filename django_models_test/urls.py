from django.conf.urls import patterns, url
from django_models_test.views import PersonsView

urlpatterns = patterns(
    '',
    url(r'^$', PersonsView.as_view(), name='index'),
)