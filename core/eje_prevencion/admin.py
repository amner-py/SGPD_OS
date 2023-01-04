from django.contrib import admin
from .models import PlanEje,EjeTrabajo,Producto,Subproducto

@admin.register(PlanEje)
class PlanEjeAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']

@admin.register(EjeTrabajo)
class EjeTrabajoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']


@admin.register(Subproducto)
class SubproductoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['producto']
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']