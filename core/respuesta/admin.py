from django.contrib import admin
from core.respuesta.models import Respuesta


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    pass