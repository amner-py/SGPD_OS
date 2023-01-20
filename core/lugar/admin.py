from django.contrib import admin
from .models import *


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['departamento']
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]
