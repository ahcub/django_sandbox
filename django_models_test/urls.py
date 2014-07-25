from django.conf.urls import patterns, url
from django_models_test.views import PersonsView

urlpatterns = patterns(
    '',
    url(r'^$', PersonsView.as_view(), name='index'),
    url(r'^persons\?(?P<lon>\+d)&$', PersonsView.as_view(), name='person_list_location'),
)