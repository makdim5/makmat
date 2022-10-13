from django.contrib.auth.models import User
from django.db import models
from . import Lections


class Topics(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    lection = models.ForeignKey(Lections, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
