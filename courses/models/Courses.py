from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    name = models.CharField(max_length=255, null=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=100, null=True)
