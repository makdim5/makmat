from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    task_info = models.TextField(max_length=255, null=False)

    def __str__(self):
        return self.task_info


class TaskComplition(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
