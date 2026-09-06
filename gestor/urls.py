from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.hello),
    path("about/", views.about),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/new-project/", views.new_project, name="new_project"),
    path(
        "projects/<int:project_id>/delete/", views.delete_project, name="delete_project"
    ),
    path("projects/<int:project_id>/edit/", views.edit_project, name="edit_project"),
    path(
        "projects/<int:project_id>/new-task/",
        views.new_task,
        name="new_task",
    ),
]
