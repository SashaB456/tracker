from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status_list = [('Done', 'Done'), ('In progress', 'In progress'), ('Delayed', 'Delayed'), ('Deleted', 'Deleted'), ('Not started', 'Not started')]
    priority_list = [('Urgent', 'Urgent'), ('Important', 'Important'), ('Okay', 'Okay')]
    status = models.CharField(max_length=15, choices=status_list, default='Not started')
    priority = models.CharField(max_length=18, choices=priority_list, default='Okay')
    deadline = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, auto_now_add=False)