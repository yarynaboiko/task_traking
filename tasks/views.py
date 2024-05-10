from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.mixins import UserIsOwnerMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from tasks import models
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from tasks.forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(creator=self.request.user)
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return  super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_update.html"
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Task
    template_name = "tasks/delete_confirmation.html"
    success_url = reverse_lazy('task-list')



