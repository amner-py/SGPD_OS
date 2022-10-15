from django.contrib import admin
from .models import *


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    pass


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    pass


@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    pass