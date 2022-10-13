from django.urls import path, include
from rest_framework import routers

from userswork import views

router = routers.SimpleRouter()
router.register(r'', views.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]