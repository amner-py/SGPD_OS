from django.db import models
from ..delegacion.models import Delegacion
from datetime import datetime


class Notificacion(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    motivo=models.CharField(verbose_name='Motivo',db_column='MOTIVO',max_length=50,null=False,blank=False)
    mensaje=models.CharField(verbose_name='Mensaje',db_column='MENSAJE',max_length=350,null=False,blank=True)
    receptor=models.ForeignKey(Delegacion,verbose_name='Receptor',db_column='RECEPTOR',on_delete=models.CASCADE)
    leido=models.BooleanField(verbose_name='Leído',db_column='LEIDO',default=False)
    fechahora=models.DateTimeField(verbose_name='Feha y Hora',db_column='FECHA_HORA',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='NOTIFICACION'
        verbose_name='Notificación'
        verbose_name_plural='Notificaciones'


    def __str__(self):
        return f'{self.mensaje}'
