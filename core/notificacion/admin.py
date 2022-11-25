from django.contrib import admin
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display=['motivo','mensaje','receptor','fechahora']
    list_filter=['receptor']
    list_editable=[]
    list_per_page=15
    search_fields=[]
