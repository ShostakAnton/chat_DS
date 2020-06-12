from django.shortcuts import render

from rest_framework.views import APIView        # писать классы rest фреймворка
from rest_framework.response import Response    # для вывода ответа на клиенскую часть
from rest_framework import permissions      # проверка аудинтефикации пользователя

from .models import Room, Chat
from chat_room.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers,  UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    def get(self, request):
        rooms = Room.objects.all()      # выбор всех комнат
        serializer = RoomSerializers(rooms, many=True)      # many - для выборки всех связующих моделей
        return Response({'date': serializer.data})


class Dialog(APIView):
    """Диалог чата, сообщение"""

    # permission_classes = [permissions.IsAuthenticated, ]        # доступ для авторизованых пользователей
    # permission_classes = [permissions.AllowAny, ]             # доступ для всех пользователей

    def get(self, request):
        room = request.GET.get("room")         # номер комнаты
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)

        return Response({"data": serializer.data})

    def post(self, request):            # что бы на бек-енде принимать данные сообщения
        # room = request.data.get("room")

        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)     # сохроняем сообщение, передаем юзера к которому будет привязано данное сообщение
            return Response({'status': 'Add'})
        else:
            return Response({'status': 'Error'})
