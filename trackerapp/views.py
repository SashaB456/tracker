from django.shortcuts import render
from .mixins import UserIsOwnerMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'taskapp/task_list.html'
    context_object_name = 'tasks'

    #def get_queryset(self):
    #    queryset = Task.objects.exclude(status='Done')
    #    return queryset
class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskapp/task_detail.html'
    context_object_name = 'task'
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskapp/task_create.html'
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
class TaskEditView(UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskapp/task_create.html'
    def get_success_url(self):
        return reverse('task-list', kwargs={"pk": self.get_object().pk})
class TaskDeleteView(UserIsOwnerMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'taskapp/task_delete.html'