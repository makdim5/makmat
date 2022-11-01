from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("courses/", include("courses.urls")),
    path("users/", include("userswork.urls")),
    path('api/token/obtain', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/drf-auth/', include('rest_framework.urls'))
]
