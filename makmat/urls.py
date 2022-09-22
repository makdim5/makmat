from django.contrib import admin
from django.urls import path, include

from topics.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("topics.urls")),
]

handler404 = page_not_found

