from django.contrib import admin
from .models import Formulario,SeccionFormulario,Pregunta,Opcion,PreguntaAuxiliar,Validacion


# INLINES
class OpcionInline(admin.TabularInline):
    model=Opcion

class ValidacionInline(admin.TabularInline):
    model=Validacion


# SITES REGISTERS
@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(PreguntaAuxiliar)
class PreguntaAuxiliarAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(SeccionFormulario)
class SeccionAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines=[OpcionInline,ValidacionInline]
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Opcion)
class PreguntaAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]