from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from models_.forms import ImageForm
from models_.models import Person, Document
from models_.constanst import *


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
            return render(request, 'models/persons_list.html', {'object_list': Person.objects.all()})
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


def document(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Document(image=request.FILES['image_file'])
            image.save()

            return HttpResponseRedirect(reverse('models_:document'))
    else:
        form = ImageForm()

    return render(request, 'models/document_form.html', {'form': form})


def index(request):
    return render(request, 'models/index.html', {'urls_list': urlpatterns})