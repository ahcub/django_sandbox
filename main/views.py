from django.shortcuts import render
from django.http import HttpResponse
from django_sandbox.settings import INSTALLED_APPS


def index(request):
    context = {
        'installed_apps': [app for app in INSTALLED_APPS if 'django.' not in app and app != 'main']
    }
    return render(request, 'main/index.html', context)