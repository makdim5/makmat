from django.contrib.auth.models import User
from rest_framework import viewsets, status
from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework import views, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UsersSerializer, LoginSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = (IsAdminUser,)


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"msg": str(user)}, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({"msg": "Logout well!"}, status=status.HTTP_202_ACCEPTED)


class RegisterView(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)


class CurrentUserView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication, )

    def get(self, request):
        return Response({
            'data': UsersSerializer(request.user).data
        })
