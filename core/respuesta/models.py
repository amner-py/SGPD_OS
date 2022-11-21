from django.db import models
from datetime import datetime
from ..delegacion.models import Delegacion
from ..formulario.models import Pregunta,Formulario
from ..asignacion.models import MetaMensual


class Respuesta(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    meta=models.ForeignKey(MetaMensual,verbose_name='Meta mensual alcanzada',db_column='META_ALCANZADA_ID',on_delete=models.SET_NULL,null=True,blank=True)
    respondido=models.DateTimeField(verbose_name='Fecha de respuesta',db_column='FECHA_RESPONDIDO',default=datetime.now,editable=False)
    latitud=models.CharField(verbose_name='Latitud',db_column='LATITUD',max_length=25,blank=False,null=False)
    longitud=models.CharField(verbose_name='Longitud',db_column='LONGITUD',max_length=25,blank=False,null=False)
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE,null=True)


    class Meta:
        db_table='RESPUESTA'
        verbose_name='RESPUESTA'
        verbose_name_plural='RESPUESTAS'


    def __str__(self):
        return f'{self.id}-{self.delegacion}-{self.formulario}'

    def delete(self,*args,**kwargs):
        print('Hola desde borrado')
        meta=MetaMensual.objects.filter(delegacion=self.delegacion).last()
        if meta:
            print(meta)
            meta.meta_alcanzada-=1
            meta.actualizado=datetime.now()
            meta.save()
            self.meta=meta
        super(Respuesta,self).delete(*args,**kwargs)

    def save(self,*args,**kwargs):
        meta=MetaMensual.objects.filter(delegacion=self.delegacion).last()
        if meta:
            meta.meta_alcanzada+=1
            meta.actualizado=datetime.now()
            meta.save()
            self.meta=meta
        super(Respuesta,self).save(*args,**kwargs)

class DetalleRespuesta(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    detalle=models.CharField(verbose_name='Respuesta',db_column='RESPUESTA',max_length=350,null=False,blank=True)
    respuesta=models.ForeignKey(Respuesta,verbose_name='Respuesta de Formulario',db_column='RESPUESTA_ID',on_delete=models.CASCADE)
    pregunta=models.ForeignKey(Pregunta,verbose_name='Pregunta',db_column='PREGUNTA_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='DETALLE_RESPUESTA'
        verbose_name='DETALLE DE RESPUESTA'
        verbose_name_plural='DETALLES DE RESPUESTA'


    def __str__(self):
        return f'{self.pregunta.enunciado}: {self.detalle}'