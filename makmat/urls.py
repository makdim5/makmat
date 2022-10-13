from django.urls import path, include

from courses.views import *

urlpatterns = [
    path("courses/", include("courses.urls")),
    path("users/", include("userswork.urls"))
]
