from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models


class Delegacion(AbstractUser):
    nombre_delegacion=models.CharField(db_column='nombre_delegacion',max_length=35)

    class Meta:
        db_table='DELEGACION'
        verbose_name='DELEGACION'
        verbose_name_plural='DELEGACIONES'


    def __str__(self):
        return f'{self.nombre_delegacion}' if self.nombre_delegacion else f'Usuario: {self.username}'