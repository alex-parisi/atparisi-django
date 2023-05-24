from django.shortcuts import render

from projects.models import Project


def project_index(request):

    projects = Project.objects.all()

    card_delays = [""] * len(projects)
    for i in range(len(projects)):
        card_delays[i] = f"animation-delay:{(i / (max(2, len(projects)) - 1)) / 2}s;"

    for i, project in enumerate(projects):
        project.card_delay = card_delays[i]

    context = {
        'projects': projects,
        'card_delays': card_delays,
    }

    return render(request, 'project_index.html', context)


def project_detail(request, pk):

    projects = Project.objects.all()
    project = Project.objects.get(pk=pk)

    context = {
        'projects': projects,
        'project': project,
    }

    return render(request, project.project_content, context)
