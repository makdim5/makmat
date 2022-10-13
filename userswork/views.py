from django.contrib.auth.models import User
from rest_framework import viewsets

from userswork.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
