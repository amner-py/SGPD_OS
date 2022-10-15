from django.contrib import admin
from .models import *


@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    pass


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoCampo)
class TipoCampoAdmin(admin.ModelAdmin):
    pass


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    pass