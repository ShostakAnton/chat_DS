from django.shortcuts import render

from rest_framework.views import APIView        # писать классы rest фреймворка
from rest_framework.response import Response    # для вывода ответа на клиенскую часть
from rest_framework import permissions      # проверка аудинтефикации пользователя

from .models import Room
from .serializers import RoomSerializers


class Rooms(APIView):
    """Комнаты чата"""
    def get(self, request):
        rooms = Room.objects.all()      # выбор всех комнат
        serializer = RoomSerializers(rooms, many=True)      # many - для выборки всех связующих моделей
        return Response({'date': serializer.data})



