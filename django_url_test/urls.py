from django.conf.urls import patterns, url
from django_url_test import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^req$', views.q_request_handler, name='q_handler'),
)