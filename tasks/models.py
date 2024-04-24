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

    title = models.CharField(max_length=250, verbose_name="Завдання")
    description = models.TextField(verbose_name="Опис")
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="todo", verbose_name="Статус")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISES, default="medium", verbose_name="Пріоритет")
    due_date = models.DateField(null=True, blank=True,verbose_name="Дата виконання")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks",verbose_name="Творець")

    def __str__(self):
        return self.title
