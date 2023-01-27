from django.contrib import admin
from .models import SeccionInicio,ImgInicio,RedSocial


@admin.register(SeccionInicio)
class SeccionAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['titulo','informacion']


@admin.register(ImgInicio)
class ImgAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=['seccion']
    list_editable=[]
    list_per_page=15
    search_fields=[]


@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display=['__str__']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=[]