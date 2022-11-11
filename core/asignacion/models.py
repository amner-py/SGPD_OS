from django.db import models
from ..delegacion.models import Delegacion
from ..lugar.models import Lugar
from ..notificacion.models import Notificacion
from datetime import datetime


class Asignacion(models.Model):
    delegacion=models.OneToOneField(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    lugar=models.OneToOneField(Lugar,verbose_name='Lugar',db_column='LUGAR_ID',on_delete=models.CASCADE)
    fecha=models.DateField(db_column='FECHA',verbose_name='Fecha',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='ASIGNACION'
        verbose_name='ASIGNACION'
        verbose_name_plural='ASIGNACIONES'


    def __str__(self):
        return f'{self.delegacion} - {self.lugar.direccion}'

    def save(self,*args,**kwargs):
        super(Asignacion,self).save(*args,**kwargs)
        Notificacion.objects.create(motivo='NUEVA ASIGNACION',mensaje=f'Se le ha asignado a: {self.lugar.municipio} la fecha {self.fecha.day}/{self.fecha.month}/{self.fecha.year}',receptor=self.delegacion)

    
class MetaMensual(models.Model):
    MES_CHOICE=[
        ('1','Enero'),
        ('2','Febrero'),
        ('3','Marzo'),
        ('4','Abril'),
        ('5','Mayo'),
        ('6','Junio'),
        ('7','Julio'),
        ('8','Agosto'),
        ('9','Septiembre'),
        ('10','Octubre'),
        ('11','Noviembre'),
        ('12','Diciembre'),
    ]
    meta=models.PositiveBigIntegerField(verbose_name='Meta mensual',db_column='META_MES')
    mes=models.CharField(verbose_name='Mes',db_column='MES',choices=MES_CHOICE,max_length=15)
    delegacion=models.OneToOneField(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='META_MENSUAL'
        verbose_name='META MENSUAL'
        verbose_name_plural='META MENSUALES'

    def __str__(self):
        return f'{self.meta} - {self.mes}'

    
    def save(self,*args,**kwargs):
        super(MetaMensual,self).save(*args,**kwargs)
        Notificacion.objects.create(motivo='NUEVA META',mensaje=f'Se le ha asignado la meta: {self.meta} para el mes {self.mes}',receptor=self.delegacion)
 


class MetaDiariaAlcanzada(models.Model):
    meta_alcanzada=models.PositiveBigIntegerField(verbose_name='Meta alcanzada',db_column='META_ALCANZADA')
    fecha=models.DateTimeField(verbose_name='Fecha',db_column='FECHA',default=datetime.now)
    meta_mensual=models.ForeignKey(MetaMensual,verbose_name='Meta mensual', db_column='META_MENSUAL',on_delete=models.CASCADE)
    alcanzada=models.BooleanField(verbose_name='Alcanzada',db_column='ALCANZADA',default=False)
    superada=models.BooleanField(verbose_name='Superada',db_column='SUPERADA',default=False)
    diferencia=models.BigIntegerField(verbose_name='Diferencia',db_column='DIFERENCIA')


    class Meta:
        db_table='META_DIARIA_ALCANZADA'
        verbose_name='META DIARIA ALCANZADA'
        verbose_name_plural='META DIARIA ALCANZADAS'

    
    def __str__(self):
        return f'{self.meta_alcanzada}'