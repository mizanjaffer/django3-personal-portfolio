from django.shortcuts import render
from .models import Project


def HomePageView(request):
    #to create home page
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
