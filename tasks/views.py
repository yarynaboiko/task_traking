from django.shortcuts import render
from django.urls import reverse_lazy

from tasks import models
from django.views.generic import ListView, DeleteView, CreateView

from tasks.forms import TaskForm


class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
