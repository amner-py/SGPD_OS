from django.contrib import admin
from .models import LugarPriorizado,MetaMensualEP


@admin.register(LugarPriorizado)
class LugarPriorizadoAdmin(admin.ModelAdmin):
    list_display=['__str__','delegacion']
    list_filter=['delegacion','lugar']
    list_editable=[]
    list_per_page=15
    search_fields=[]

@admin.register(MetaMensualEP)
class MetaMensualEPAdmin(admin.ModelAdmin):
    list_display=['__str__','delegacion']
    list_filter=['asignado','delegacion','estado']
    list_editable=[]
    list_per_page=15
    search_fields=[]
