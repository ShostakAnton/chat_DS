from django.contrib import admin
from . models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creater", "invited_user", "date")      # отображаемые поля в админ панеле

    def invited_user(self, obj):      # обработка всех наших пользователей, которые были приглашены в данную комнату, obj - это комната
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
