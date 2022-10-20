from django.contrib import admin
from .models import Notificacion,Destinatario

class DestinatarioInline(admin.TabularInline):
    model=Destinatario

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    inlines=[DestinatarioInline]
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]
    