from django.contrib import admin
from .models import Asignacion,MetaMensualEP, MetaMensualAO


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display=['id','__str__','delegacion']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]

@admin.register(MetaMensualEP)
class MetaMensualEPAdmin(admin.ModelAdmin):
    list_display=['__str__','delegacion']
    list_filter=['asignado']
    list_editable=[]
    list_per_page=15
    search_fields=[]

@admin.register(MetaMensualAO)
class MetaMensualAOAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['asignado']
    list_editable=[]
    list_per_page=15
    search_fields=[]
