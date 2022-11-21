
from django.db import models
from django.core.exceptions import ValidationError
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
    ESTADO_CHOICE=[
        ('na','No alcanzado'),
        ('a','Alcanzado'),
        ('s','Superado')
    ]
    _ACTUALIZAR=False
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    meta=models.PositiveBigIntegerField(verbose_name='Meta mensual',db_column='META_MES')
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    meta_alcanzada=models.PositiveBigIntegerField(verbose_name='Meta alcanzada',db_column='META_ALCANZADA',default=0)
    asignado=models.DateTimeField(verbose_name='Fecha de creación',db_column='FECHA_ASIGNADO',default=datetime.now)
    estado=models.CharField(verbose_name='Estado',db_column='ESTADO',max_length=15,choices=ESTADO_CHOICE,default=ESTADO_CHOICE[0][0])
    actualizado=models.DateTimeField(verbose_name='Fecha de actualización',db_column='FECHA_ACTUALIZADO',default=datetime.now)
    diferencia=models.BigIntegerField(verbose_name='Diferencia',db_column='DIFERENCIA',blank=True)


    class Meta:
        db_table='META_MENSUAL_ALCANZADA'
        verbose_name='META MENSUAL'
        verbose_name_plural='META MENSUALES'

    
    def __str__(self):
            if self.estado=='na':
                return f'No alcanzada por {self.diferencia*-1}'
            elif self.estado=='a':
                return f'Meta de {self.meta} alcanzada'
            elif self.estado=='s':
                return f'Superada por {self.diferencia}'


    def clean(self):
        try:
            anterior=MetaMensual.objects.filter(delegacion=self.delegacion).last()
            if anterior:
                if anterior.asignado.month == self.asignado.month:
                        if self.asignado.year == anterior.asignado.year:
                            if self.id == anterior.id:
                                self._ACTUALIZAR=True
                            else:
                                raise ValidationError('No puede agregar una nueva meta a este mes, favor de esperar al siguiente mes.')
        except:
            raise ValidationError('Debe completar los campos requeridos.')

    def save(self,*args,**kwargs):
        if self._ACTUALIZAR:
            super(MetaMensual,self).save(*args,**kwargs)
            Notificacion.objects.create(motivo='META MODIFICADA',mensaje=f'Se le ha actualizado la meta para el mes {self.asignado.month} de {self.meta}',receptor=self.delegacion)
        else:
            diferencia=self.meta_alcanzada-self.meta
            self.diferencia=diferencia
            print(f'LA DIFERENCIA ES DE: {self.diferencia}')
            if self.diferencia>0:
                self.estado='s'
            elif self.diferencia==0:
                self.estado='a'
            else:
                self.estado='na'
            super(MetaMensual,self).save(*args,**kwargs)
            Notificacion.objects.create(motivo='NUEVA META ASIGNADA',mensaje=f'Se le ha sido asignada una nueva meta de {self.meta} para el mes {self.asignado.month}.',receptor=self.delegacion)