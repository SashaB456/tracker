from django.urls import path, include
from . import views
urlpatterns = [
    path('task-list/', views.TaskListView.as_view(),  name='task-list'),
]