from django.contrib import admin
from .models import *


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    pass