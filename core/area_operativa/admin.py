from django.contrib import admin
from .models import PlanArea,TipoOperativo

@admin.register(TipoOperativo)
class TipoOperativoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']

@admin.register(PlanArea)
class PlanAreaAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']