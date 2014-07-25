from django.views import generic
from django_models_test.models import Person


def get_persons(request):
    pass


def get_persons_by_location(request, lon, lat, masl=None):
    lon = request.GET['lon']
    lat = request.GET['lat']
    masl = request.GET['masl']


def get_persons_by_name(request, name):
    pass


class PersonsView(generic.ListView):
    model = Person
    template_name = 'models/persons_list.html'
