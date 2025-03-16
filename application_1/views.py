import os

from django.shortcuts import *
from application_1.models import Database
from application_1.function import *


# Create your views here.

def request_5(request):
    if request.method == 'POST':
        v = Database(x=request.POST['x'], y=request.POST['y'])
        v.save()
        return HttpResponseRedirect(reverse('app4'))
    else:
        # return render(request, 'input_html_1.html')
        return render(request, 'input_html_1.html', context={'data': Database.objects.all()})


def request_3(request):
    return render(request, 'main.html')


def request_4(request):
    return render(request, 'main_2.html')


def request_6(request):
    return render(request, template_name='data.html', context={'data': Database.objects.all()})


# def request_5(request):
#     return render(request, 'main_2.html')

def request_7(request):
    return render(request, template_name='api_1.html', context={'file_name': func()})
