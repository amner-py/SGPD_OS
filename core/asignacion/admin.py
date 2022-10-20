from django.contrib import admin
from .models import Asignacion


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]