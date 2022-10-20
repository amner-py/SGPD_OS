from django.contrib import admin
from core.respuesta.models import Respuesta


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]