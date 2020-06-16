from django.shortcuts import render
from django.db.models import Q  # что бы создать запрос или
from rest_framework.views import APIView  # писать классы rest фреймворка
from rest_framework.response import Response  # для вывода ответа на клиенскую часть
from rest_framework import permissions  # проверка аудинтефикации пользователя

from django.contrib.auth.models import User

from .models import Room, Chat
from chat_room.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]  # доступ для авторизованых пользователей

    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))  # выбор тех комнат, где ты или
        # создатель или приглашенный
        serializer = RoomSerializers(rooms, many=True)  # many - для выборки всех связующих моделей
        return Response({'date': serializer.data})


class Dialog(APIView):
    """Диалог чата, сообщение"""

    permission_classes = [permissions.IsAuthenticated, ]  # доступ для авторизованых пользователей

    # permission_classes = [permissions.AllowAny, ]             # доступ для всех пользователей

    def get(self, request):
        room = request.GET.get("room")  # номер комнаты
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)

        return Response({"data": serializer.data})

    def post(self, request):  # что бы на бек-енде принимать данные сообщения
        # room = request.data.get("room")

        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(
                user=request.user)  # сохроняем сообщение, передаем юзера к которому будет привязано данное сообщение
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    """Добавление юзеров в комнату чата"""

    def get(self, request):  # возвращение списка всех пользователей
        users = User.objects.all()  # с базы список всех пользователей
        serializer = UserSerializer(users, many=True)  # сериализация пользователей
        return Response(serializer.data)

    def post(self, request):  # добавлнение пользователя в комнату
        room = request.data.get("room")  # id комнаты
        user = request.data.get("user")  # id пользователя
        try:
            room = Room.objects.get(id=room)  # комната с id данной комнаты
            room.invited.add(user)  # добавление пользователя в комнату
            room.save()  # сохранение
            return Response(status=201)
        except:
            return Response(status=400)
