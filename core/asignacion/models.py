from django.db import models
from ..delegacion.models import Delegacion
from ..lugar.models import Lugar
from datetime import datetime


class Asignacion(models.Model):
    delegacion=models.OneToOneField(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',unique=True,on_delete=models.CASCADE)
    lugar=models.OneToOneField(Lugar,verbose_name='Lugar',db_column='LUGAR_ID',unique=True,on_delete=models.CASCADE)
    fecha=models.DateField(db_column='FECHA',verbose_name='Fecha',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='ASIGNACION'
        verbose_name='ASIGNACION'
        verbose_name_plural='ASIGNACIONES'


    def __str__(self):
        return f'{self.delegacion} - {self.lugar.direccion}'