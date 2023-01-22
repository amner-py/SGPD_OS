from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario,Delegacion
from .forms import UsuarioCreateForm,UsuarioChangeForm


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form=UsuarioChangeForm
    add_form=UsuarioCreateForm
    fieldsets=UserAdmin.fieldsets + (
        (
            'Información',{
                'fields':(
                    'delegacion',
                    'fecha_nacimiento'
                )
            }
        ),
    )
    list_display=[
        'username',
        'first_name',
        'delegacion'
    ]
    list_editable=['delegacion']

@admin.register(Delegacion)
class DelegacionAdmin(admin.ModelAdmin):
    list_display=['nombre']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']