from django.db import models
from django.core.exceptions import ValidationError
from ..delegacion.models import Delegacion,Usuario
from ..lugar.models import Lugar
from ..notificacion.models import Notificacion
from ..eje_prevencion.models import EjeTrabajo
from datetime import datetime


class LugarPriorizado(models.Model):
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    lugar=models.ForeignKey(Lugar,verbose_name='Lugar',db_column='LUGAR_ID',on_delete=models.CASCADE)
    fecha=models.DateField(db_column='FECHA',verbose_name='Fecha',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='LUGAR_PRIORIZADO'
        verbose_name='Lugar Priorizado'
        verbose_name_plural='Lugares Priorizados'


    def __str__(self):
        return f'{self.lugar}'

    def save(self,*args,**kwargs):
        super(LugarPriorizado,self).save(*args,**kwargs)
        usuarios=Usuario.objects.filter(delegacion=self.delegacion)
        for usuario in usuarios:
            Notificacion.objects.create(motivo=f'NUEVA ASIGNACION EN {self.__str__}'.upper,mensaje=f'Se le ha asignado a: {self.lugar.municipio} la fecha {self.fecha.day}/{self.fecha.month}/{self.fecha.year}',receptor=usuario)


class MetaMensualEP(models.Model):
    ESTADO_CHOICE=[
        ('na','No alcanzado'),
        ('a','Alcanzado'),
        ('s','Superado')
    ]
    _ACTUALIZAR=False
    _NUEVO=False
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    meta=models.PositiveBigIntegerField(verbose_name='Meta mensual',db_column='META_MES')
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    eje=models.ForeignKey(EjeTrabajo,verbose_name='Eje de Trabajo',db_column='eje',on_delete=models.CASCADE)
    meta_alcanzada=models.PositiveBigIntegerField(verbose_name='Meta alcanzada',db_column='META_ALCANZADA',default=0)
    asignado=models.DateTimeField(verbose_name='Fecha de creación',db_column='FECHA_ASIGNADO',default=datetime.now)
    estado=models.CharField(verbose_name='Estado',db_column='ESTADO',max_length=15,choices=ESTADO_CHOICE,default=ESTADO_CHOICE[0][0])
    actualizado=models.DateTimeField(verbose_name='Fecha de actualización',db_column='FECHA_ACTUALIZADO',default=datetime.now)
    diferencia=models.BigIntegerField(verbose_name='Diferencia',db_column='DIFERENCIA',blank=True)
    

    class Meta:
        db_table='META_MENSUAL_EJE_PREVENCION'
        verbose_name='Meta mensual eje de prevención'
        verbose_name_plural='Metas mensuales eje de prevención'

    
    def __str__(self):
            if self.estado=='na':
                return f'No alcanzada por {self.diferencia*-1}'
            elif self.estado=='a':
                return f'Meta de {self.meta} alcanzada'
            elif self.estado=='s':
                return f'Superada por {self.diferencia}'


    def clean(self):
        try:
            anteriores=MetaMensualEP.objects.filter(delegacion=self.delegacion)
            if anteriores:
                for anterior in anteriores:
                    if self.id == anterior.id:
                        if self.meta_alcanzada != anterior.meta_alcanzada:
                            self._NUEVO=True
                        else:
                            self._ACTUALIZAR=True
        except Exception as e:
            print(e)
            raise ValidationError('Debe completar los campos requeridos.')

    def save(self,*args,**kwargs):
            diferencia=self.meta_alcanzada-self.meta
            self.diferencia=diferencia
            if self.diferencia>0:
                self.estado='s'
            elif self.diferencia==0:
                self.estado='a'
            else:
                self.estado='na'
            super(MetaMensualEP,self).save(*args,**kwargs)
            if self._ACTUALIZAR:
                usuarios=Usuario.objects.filter(delegacion=self.delegacion)
                for usuario in usuarios:
                    Notificacion.objects.create(motivo=f'META PARA {self.eje.nombre.upper()} MODIFICADA',mensaje=f'Se le ha actualizado la meta para el mes {self.asignado.month} de {self.meta}',receptor=usuario)
            elif self._NUEVO:
                pass
            else:
                usuarios=Usuario.objects.filter(delegacion=self.delegacion)
                for usuario in usuarios:
                    Notificacion.objects.create(motivo=f'NUEVA META PARA {self.eje.nombre.upper()} ASIGNADA',mensaje=f'Se le ha sido asignada una nueva meta de {self.meta} para el mes {self.asignado.month}.',receptor=usuario)
