from django.db import models

from courses.models import Topics, Sections, Tasks
from courses.models.Courses import Courses


class Orders(models.Model):
    order = models.IntegerField(null=False)


class CourseSectionOrders(Orders):
    course = models.ForeignKey(Courses, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Sections, null=True, on_delete=models.SET_NULL)


class SectionTopicOrders(Orders):
    topic = models.ForeignKey(Topics, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Sections, null=True, on_delete=models.SET_NULL)


class TopicTaskOrders(Orders):
    topic = models.ForeignKey(Topics, null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Tasks, null=True, on_delete=models.SET_NULL)
