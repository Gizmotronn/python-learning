from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all() # perform a query. A query is simply a command that allows you to create, retrieve, update, or delete objects (or rows) in your database. In this case, you’re retrieving all objects in the projects table.
    context = {# https://realpython.com/get-started-with-django-1/#showcase-your-projects
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)    