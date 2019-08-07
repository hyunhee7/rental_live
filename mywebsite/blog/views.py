from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import info
# Create your views here.
def index(req):
    context = {

    }
    return render(req, "index.html", context=context)

def person(req):
    user_id = req.POST["user_id"]

    context = {
        'user_id':user_id
    }
    return render(req, "person.html", context)

def list(req):
    context = {

    }
    return render(req, "list.html", context=context)
def recommand(req):
    context = {

    }
    return render(req, "recommand.html", context=context)

