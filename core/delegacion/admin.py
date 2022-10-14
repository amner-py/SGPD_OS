from distutils import core
from django.contrib import admin
from .models import Delegacion,Img

@admin.register(Delegacion)
class DelegacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    pass