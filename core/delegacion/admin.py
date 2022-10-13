from distutils import core
from django.contrib import admin
from .models import Delegacion

@admin.register(Delegacion)
class DelegacionAdmin(admin.ModelAdmin):
    pass
