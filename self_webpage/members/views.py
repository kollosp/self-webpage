from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

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
    return HttpResponse(template.render(context={
        "user": request.user
    }, request=request))

def login(request):
    if request.method == 'POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        else:
            # return incorrect credentials info
            return HttpResponse(loader.get_template('login.html').render(context={
                "message" : "Wrong email or password"
            }, request=request))
    else:
        print("get")

        return HttpResponse(loader.get_template('login.html').render(context={
                    "message" : ""
        }, request=request))

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))