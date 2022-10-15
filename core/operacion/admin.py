from django.contrib import admin
from .models import *


@admin.register(Operacion)
class OperacionAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoOperativo)
class TipoOperativoAdmin(admin.ModelAdmin):
    pass


@admin.register(EjeTrabajo)
class EjeTrabajoAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Subproducto)
class SubproductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass