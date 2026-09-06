from django.db import models


# Create your models here.
class Project(models.Model):
    """
    Modelo que representa un proyecto.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()


class Task(models.Model):
    """
    Modelo que representa una tarea asociada a un proyecto.
    """

    PRIORITY_CHOICES = [
        ("low", "Baja"),
        ("medium", "Media"),
        ("high", "Alta"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("in_progress", "En progreso"),
        ("completed", "Completada"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
