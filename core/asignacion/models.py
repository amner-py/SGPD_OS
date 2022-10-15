from django.db import models
from delegacion.models import Delegacion
from lugar.models import Lugar


class Asignacion(models.Model):
    delegacion=models.ForeignKey(Delegacion,db_column='DELEGACION_ID',primary_key=True,on_delete=models.CASCADE)
    lugar=models.ForeignKey(Lugar,db_column='LUGAR_ID',primary_key=True,on_delete=models.CASCADE)
    fecha=models.DateField(db_column='FECHA',blank=False,null=False)

    class Meta:
        db_table='ASIGNACION'
        verbose_name='ASIGNACION'
        verbose_name_plural='ASIGNACIONES'


    def __str__(self):
        return f'{self.delegacion} - {self.lugar.direccion}'