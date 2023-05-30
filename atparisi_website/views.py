import string
from django.shortcuts import render
from projects.models import Project


def home(request):

    projects = Project.objects.all()

    context = {'projects': projects}

    return render(request, 'home.html', context)
