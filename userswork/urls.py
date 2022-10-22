from django.urls import path, include
from rest_framework import routers

from userswork import views

router = routers.DefaultRouter()
router.register(r'', views.UsersViewSet)


urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('current', views.CurrentUserView.as_view()),
    path('', include(router.urls))

]
