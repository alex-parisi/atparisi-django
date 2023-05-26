import string
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
    tags = [f"#{x}" for x in project.tags.split(', ')]
    if tags == ['#']:
        tags = ""
    tag_labels = []
    for tag in tags:
        tag = string.capwords(tag[1::].replace('-', ' '))
        tag_labels.append(tag)
    tag_delays = []
    for i in range(len(tag_labels)):
        tag_delays.append(f"animation-delay:{(i / 6)}s;")
    tag_ids = [f"{x}_btn" for x in project.tags.split(', ')]
    tags = zip(tags, tag_labels, tag_delays, tag_ids)
    context = {
        'projects': projects,
        'project': project,
        'tags': tags,
    }

    return render(request, project.project_content, context)
