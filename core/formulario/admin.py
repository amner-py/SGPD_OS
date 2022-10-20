from django.contrib import admin
from .models import Formulario,SeccionFormulario,TipoCampo,Pregunta,Opcion


# INLINES
class PreguntaInline(admin.TabularInline):
    model=Pregunta


# SITES REGISTERS
@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    inlines=[PreguntaInline]
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


@admin.register(TipoCampo)
class TipoCampoAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
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