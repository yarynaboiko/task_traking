from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOISES = [
        ("todo", "Потрібно зробити"),
        ("in_progress", "В процесі"),
        ("done", "Виконано"),
    ]

    PRIORITY_CHOISES = [
        ("low", "Низький"),
        ("medium", "Середній"),
        ("high", "Високий"),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
