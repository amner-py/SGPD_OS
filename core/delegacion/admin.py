from distutils import core
from django.contrib import admin
from .models import Delegacion

@admin.register(Delegacion)
class DelegacionAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]

