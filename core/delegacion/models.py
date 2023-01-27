from django.contrib.auth.models import AbstractUser
from django.db import models


class Delegacion(models.Model):
    nombre=models.CharField(verbose_name='Nombre',db_column='nombre',max_length=35,blank=True)

    class Meta(AbstractUser.Meta):
        db_table='DELEGACION'
        verbose_name='Delegación'
        verbose_name_plural='Delegaciones'

    def __str__(self):
        return f'{self.nombre}'

class Usuario(AbstractUser):
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='delegacion_id',on_delete=models.CASCADE,null=True)
    fecha_nacimiento=models.DateField(verbose_name='Fecha de nacimiento',db_column='fecha_nacimiento',null=True)
    

    class Meta(AbstractUser.Meta):
        db_table='USUARIO'
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'


    def __str__(self):
        return f'{self.username}'
