from django.contrib import admin
from .models import Asignacion


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    pass