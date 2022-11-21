from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Delegacion
from .forms import DelegacionCreateForm,DelegacionChangeForm


@admin.register(Delegacion)
class DelegacionAdmin(UserAdmin):
    form=DelegacionChangeForm
    add_form=DelegacionCreateForm
    fieldsets=UserAdmin.fieldsets + (
        (
            'Delegación',{
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

