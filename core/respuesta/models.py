from django.db import models
from datetime import datetime
from ..delegacion.models import Delegacion
from ..formulario.models import Pregunta


class Respuesta(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    respuesta=models.CharField(verbose_name='Respuesta',db_column='RESPUESTA',max_length=350,null=False,blank=True)
    respondido=models.DateTimeField(verbose_name='Respondido',db_column='FECHA_RESPONDIDO',default=datetime.now,editable=False)
    latitud=models.CharField(verbose_name='Latitud',db_column='LATITUD',max_length=12,blank=False,null=False)
    longitud=models.CharField(verbose_name='Longitud',db_column='LONGITUD',max_length=13,blank=False,null=False)
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    pregunta=models.ForeignKey(Pregunta,verbose_name='Pregunta',db_column='PREGUNTA_ID',on_delete=models.CASCADE)


    class Meta:
        db_table='RESPUESTA'
        verbose_name='RESPUESTA'
        verbose_name_plural='RESPUESTAS'


    def __str__(self):
        return f'{self.respuesta}'

    '''
    def save(self, force_insert, force_update, using, update_fields):
        valor=super().save(force_insert, force_update, using, update_fields)

        respuestas_hechas=len(Respuesta.objects.all())
        if respuestas_hechas<0:
            meta_mensual_id=MetaMensual.objects.filter(mes=datetime.month,delegacion=self.delegacion)
            diferencia_metas=meta_mensual_id-respuestas_hechas
            if diferencia_metas>0:
                meta_diaria_alcanzada=MetaDiariaAlcanzada(meta_alcanzada=respuestas_hechas,meta_mensual=meta_mensual_id)

        return valor

'''