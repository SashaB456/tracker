from django.shortcuts import render
from .models import Task
from django.views.generic import ListView
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'taskapp/task_list.html'
    context_object_name = 'tasks'
def create_task(request):
    if request.method == 'POST':
        name = request.POST.get("title", default='Title')