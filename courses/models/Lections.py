from django.db import models


class Lections(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    text = models.TextField()

