from django.db import models
from datetime import datetime
from core.delegacion.models import Delegacion
from core.formulario.models import Pregunta


class Respuesta(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    respuesta=models.CharField(db_column='RESPUESTA',max_length=350,null=False,blank=True)
    respondido=models.DateTimeField(db_column='FECHA_RESPONDIDO',default=datetime.now,editable=False)
    latitud=models.CharField(db_column='LATITUD',max_length=12,blank=False,null=False)
    longitud=models.CharField(db_column='LONGITUD',max_length=13,blank=False,null=False)
    delegacion=models.ForeignKey(Delegacion,db_column='DELEGACION_ID',on_delete=models.CASCADE)
    pregunta=models.ForeignKey(Pregunta,db_column='PREGUNTA_ID',on_delete=models.CASCADE)


    class Meta:
        db_table='RESPUESTA'
        verbose_name='RESPUESTA'
        verbose_name_plural='RESPUESTAS'


    def __str__(self):
        return f'{self.respuesta}'

