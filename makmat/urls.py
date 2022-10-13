from django.shortcuts import redirect
from django.urls import path, include

from courses.views import *

urlpatterns = [
    path("courses/", include("courses.urls"), name="courses"),
]
