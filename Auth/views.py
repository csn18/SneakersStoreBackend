from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserProfileVIew(APIView):
    """ Профиль пользователя """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Возвращает информацию о пользователе для профиля """
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        """ Обновления данных пользователя """
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_extra_actions(cls):
        return []
