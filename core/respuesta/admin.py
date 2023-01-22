from django.contrib import admin
from .models import EPRespuesta,AORespuesta

@admin.register(EPRespuesta)
class EPRespuestaAdmin(admin.ModelAdmin):
    list_display=['respondido','usuario','delegacion','plan','eje','producto','subproducto']
    list_filter=['respondido','usuario','delegacion','plan','eje','producto','subproducto']
    list_editable=[]
    list_per_page=15
    search_fields=[]

@admin.register(AORespuesta)
class AORespuestaAdmin(admin.ModelAdmin):
    list_display=['respondido','usuario','delegacion','plan','operativo']
    list_filter=['respondido','usuario','delegacion','plan','operativo']
    list_editable=[]
    list_per_page=15
    search_fields=[]