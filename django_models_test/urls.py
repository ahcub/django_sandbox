from django.conf.urls import patterns, url
from django_models_test import views
from django_models_test.views import PersonsView

urlpatterns = patterns(
    '',
    url(r'^$', PersonsView.as_view(), name='index'),
    url(r'^persons$', PersonsView.as_view(), name='person_list_location'),
    url(r'^document$', views.document, name='document'),
)