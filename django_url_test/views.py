from django.shortcuts import render


def index(request):
    return render(request, 'urls/index.html', {})


def q_request_handler(request):
    context = {
        'request_args': request.GET.items(),
    }
    return render(request, 'urls/request_parameters_list.html', context)