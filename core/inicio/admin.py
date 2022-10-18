from django.contrib import admin
from .models import SeccionInicio,ImgInicio,RedSocial


@admin.register(SeccionInicio)
class SeccionAdmin(admin.ModelAdmin):
    pass


@admin.register(ImgInicio)
class ImgAdmin(admin.ModelAdmin):
    pass


@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    pass