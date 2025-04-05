from django.urls import path, include
from . import views
urlpatterns = [
    path('task/list/', views.TaskListView.as_view(),  name='task-list'),
    path('task/detail/<int:pk>', views.TaskDetailView.as_view(),  name='task-detail'),
    path('task/create', views.TaskCreateView.as_view(), name='create-view'),
]