from django.contrib.auth.models import User
from django.db import models

from courses.models import Sections, Topics, Courses


class AccessEnables(models.Model):
    is_current_user_enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class UserCourseAccessEnables(AccessEnables):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class UserSectionAccessEnables(AccessEnables):
    section = models.ForeignKey(Sections, null=True, on_delete=models.SET_NULL)


class UserTopicAccessEnables(AccessEnables):
    topic = models.ForeignKey(Topics, null=True, on_delete=models.SET_NULL)
