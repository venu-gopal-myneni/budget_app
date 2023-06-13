from django.shortcuts import render

from . import models

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def user_list(request):
    users = models.User.objects.all()
    context = {"users":users}
    return render(request,"user_list.html",context)
