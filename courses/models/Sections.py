from django.contrib.auth.models import User
from django.db import models


class Sections(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
