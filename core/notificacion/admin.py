from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display=['motivo','mensaje_safe','receptor','fechahora']
    list_filter=['receptor']
    list_editable=[]
    list_per_page=15
    search_fields=[]

    def mensaje_safe(self,obj):
        return mark_safe(obj.mensaje)
    mensaje_safe.short_description='Mensaje'