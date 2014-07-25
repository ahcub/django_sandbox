from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from django_models_test.models import Person
from django_models_test.constanst import *


def get_persons(request):
    name = request.GET.get('name', None)
    if name:
        return get_persons_by_name(request, name)
    else:
        try:
            lon = float(request.GET['lon'])
            lat = float(request.GET['lat'])
            masl = request.GET.get('masl', None)
        except MultiValueDictKeyError:
            return PersonsView.as_view()
        else:
            get_persons_by_location(request, lon, lat, masl)


def get_persons_by_location(request, lon, lat, masl=None):
    filter_parameters = {
        'location__lon__range': (lon - LLR, lon + LLR),
        'location__lat__range': (lat - LLR, lat + LLR),
    }
    if masl:
        filter_parameters['location__masl__range'] = (masl - MLR, masl + MLR)

    context = {'object_list': Person.objects.filter(**filter_parameters)}
    return render(request, 'models/persons_list.html', context)


def get_persons_by_name(request, name):
    context = {
        'object_list': Person.objects.filter(name__contains=name)
    }
    return render(request, 'models/persons_list.html', context)


class PersonsView(generic.ListView):
    model = Person
    template_name = 'models/persons_list.html'
