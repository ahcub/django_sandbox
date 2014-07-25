from django.views import generic
from django_models_test.models import Person


def get_persons(request):
    pass


def get_persons_by_location(request):
    lon = request.GET['lon']
    lat = request.GET['lat']
    masl = request.GET['masl']


class PersonsView(generic.ListView):
    model = Person
    template_name = 'models/persons_list.html'
