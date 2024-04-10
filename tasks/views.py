from django.shortcuts import render
from tasks import models
from django.views.generic import ListView, DeleteView, CreateView

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
