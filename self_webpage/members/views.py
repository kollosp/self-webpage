from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member

def members(request):
    # The following line will send simple string as a server response
    # return HttpResponse("<h1>Hello world!</h1>")

    # display simple html without processing
    # template = loader.get_template('first.html')
    # return HttpResponse(template.render())

    mymembers = Member.objects.all().values()
    template = loader.get_template('all.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))