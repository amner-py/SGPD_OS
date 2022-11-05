from django.contrib import admin
from .models import Asignacion,MetaDiariaAlcanzada,MetaMensual


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]

@admin.register(MetaMensual)
class MetaMensualAdmin(admin.ModelAdmin):
    pass

@admin.register(MetaDiariaAlcanzada)
class MetaDiariaAlcanzadaAdmin(admin.ModelAdmin):
    pass