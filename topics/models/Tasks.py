from django.db import models
from django.contrib.auth.models import User

from topics.models import Topics


class Tasks(models.Model):
    task_info = models.TextField(max_length=255, null=True, verbose_name="Задание")
    correct_answer = models.CharField(max_length=5, null=True, verbose_name="Правильный ответ")
    topic = models.ForeignKey(Topics, on_delete=models.PROTECT, null=True, verbose_name="Выбор темы")

    def __str__(self):
        return self.task_info

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'
        ordering = ['topic']

    def check_task(self, answer):
        return answer == self.correct_answer


class TaskComplition(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
