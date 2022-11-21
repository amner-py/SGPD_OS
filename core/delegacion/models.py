from django.contrib.auth.models import AbstractUser
from django.db import models



class Delegacion(AbstractUser):
    delegacion=models.CharField(verbose_name='Delegación',db_column='delegacion',max_length=35,blank=True)
    fecha_nacimiento=models.DateField(verbose_name='Fecha de nacimiento',db_column='FECHA_NACIMIENTO',null=True)
    

    class Meta(AbstractUser.Meta):
        db_table='DELEGACION'
        verbose_name='DELEGACION'
        verbose_name_plural='DELEGACIONES'


    def __str__(self):
        return f'{self.delegacion}' if self.delegacion else f'{self.username}'
