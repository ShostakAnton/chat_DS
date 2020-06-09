from django.shortcuts import render

from rest_framework.views import APIView        # писать классы rest фреймворка
from rest_framework.response import Response    # для вывода ответа на клиенскую часть
from rest_framework import permissions      # проверка аудинтефикации пользователя

