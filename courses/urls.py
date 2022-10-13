from django.urls import path, include
from rest_framework import routers

from courses import views

router = routers.SimpleRouter()
router.register(r'', views.CoursesViewSet)
router.register(r'sections', views.SectionsViewSet)
router.register(r'topics', views.TopicsViewSet)
router.register(r'tasks', views.TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
