from django.contrib import admin
from .models import Respuesta,DetalleRespuesta


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['formulario','respondido','delegacion']
    list_editable=[]
    list_per_page=15
    search_fields=[]

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.delete()

@admin.register(DetalleRespuesta)
class DetalleRespuestaAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['respuesta']
    list_editable=[]
    list_per_page=15
    search_fields=['detalle']