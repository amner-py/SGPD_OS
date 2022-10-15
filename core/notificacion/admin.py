from django.contrib import admin
from .models import *


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
    pass