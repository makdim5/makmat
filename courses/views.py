from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from courses.models import Courses, Sections, Topics, Tasks
from courses.serializers import CoursesSerializer, SectionsSerializer,\
    TopicsSerializer, TasksSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAuthenticated,)


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer
    permission_classes = (IsAuthenticated,)


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    permission_classes = (IsAuthenticated,)


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)
