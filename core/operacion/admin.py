from django.contrib import admin
from .models import *


@admin.register(Operacion)
class OperacionAdmin(admin.ModelAdmin):
    list_display=['id','__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']


@admin.register(TipoOperativo)
class TipoOperativoAdmin(admin.ModelAdmin):
    list_display=['__str__','operacion']
    list_filter=['operacion']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']


@admin.register(EjeTrabajo)
class EjeTrabajoAdmin(admin.ModelAdmin):
    list_display=['__str__','operacion']
    list_filter=['operacion']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['__str__','operacion']
    list_filter=['operacion']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']


@admin.register(Subproducto)
class SubproductoAdmin(admin.ModelAdmin):
    list_display=['__str__','producto']
    list_filter=['producto']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display=['__str__','operacion']
    list_filter=['operacion']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']