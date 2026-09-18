from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Project, Task

@login_required
def hello(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("<h1>About page</h1>") 


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(
        request,
        "project_detail.html",
        {"project": project, "tasks": project.tasks.all()},
    )


def new_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        image = request.FILES.get("image")

        if name and description and duration:
            project = Project(name=name, description=description, duration=duration)
            
            if image:
                project.image = image
            project.save()

        return redirect("projects")
    return render(request, "create_project.html")


def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect("projects")


def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "POST":
        project.name = request.POST.get("name")
        project.description = request.POST.get("description")
        project.duration = request.POST.get("duration")
        project.save()
        return redirect("projects")

    return render(request, "edit_project.html", {"project": project})


def new_task(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        status = request.POST.get("status")

        if title and description and priority and status:
            Task.objects.create(
                project=project,
                title=title,
                description=description,
                priority=priority,
                status=status,
            )
        return redirect("project_detail", project_id=project.id)

    return render(
        request,
        "create_task.html",
        {
            "project": project,
            "priority_choices": Task.PRIORITY_CHOICES,
            "status_choices": Task.STATUS_CHOICES,
        },
    )


@require_POST
def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.status == "pending":
        task.status = "in_progress"
        task.save()
    elif task.status == "in_progress":
        task.status = "completed"
        task.save()

    return redirect("project_detail", project_id=task.project.id)


def update_task_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = "completed"
    task.save()
    return redirect("project_detail", project_id=task.project.id)
