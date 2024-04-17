from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="task-list"),
    path('create/', views.TaskCreateView.as_view(), name="task-create"),

]