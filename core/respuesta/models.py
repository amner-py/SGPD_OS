from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from ..delegacion.models import Delegacion,Usuario
from ..asignacion.models import LugarPriorizado,MetaMensualEP
from ..area_operativa.models import PlanArea,TipoOperativo
from ..eje_prevencion.models import PlanEje,EjeTrabajo,Producto,Subproducto

class EPRespuesta(models.Model):
    _ACTUALIZAR=False
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    meta=models.ForeignKey(MetaMensualEP,verbose_name='Meta mensual eje de prevención',db_column='META_EJE_PREVENCION',on_delete=models.SET_NULL,null=True,blank=True)
    latitud=models.CharField(verbose_name='Latitud',db_column='LATITUD',max_length=25,blank=False,null=False)
    longitud=models.CharField(verbose_name='Longitud',db_column='LONGITUD',max_length=25,blank=False,null=False)
    respondido=models.DateField(verbose_name='Fecha respondido',db_column='FECHA_CREADO',default=timezone.now)
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,verbose_name='Usuario',db_column='USUARIO_ID',on_delete=models.CASCADE)
    lugar_priorizado=models.ForeignKey(LugarPriorizado,verbose_name='Lugar priorizado',db_column='PRIORIZADO_ID',on_delete=models.CASCADE)
    lugar_no_priorizado=models.CharField(verbose_name='Lugar no priorizado',db_column='NO_PRIORIZADO',max_length=350)
    lugar_especifico=models.CharField(verbose_name='Lugar específico',db_column='LUGAR_ESPECIFICO',max_length=350)
    plan=models.ForeignKey(PlanEje,verbose_name='Plan/Orden',db_column='PLAN',on_delete=models.CASCADE)
    eje=models.ForeignKey(EjeTrabajo,verbose_name='Eje de Trabajo',db_column='EJE_TRABAJO',on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,verbose_name='Producto',db_column='PRODUCTO',on_delete=models.CASCADE)
    subproducto=models.ForeignKey(Subproducto,verbose_name='Subproducto',db_column='SUBPRODUCTO',on_delete=models.CASCADE)
    observaciones=models.TextField(verbose_name='Observaciones',db_column='OBSERVACIONES',max_length=450,blank=True)
    cantidad=models.PositiveBigIntegerField(verbose_name='Cantidad',db_column='CANTIDAD')
    cantidad_personas=models.PositiveBigIntegerField(verbose_name='Cantidad de personas',db_column='CANTIDAD_PERSONAS')
    ninios=models.PositiveBigIntegerField(verbose_name='Niños',db_column='NINIOS',default=0)
    ninias=models.PositiveBigIntegerField(verbose_name='Niñas',db_column='NINIAS',default=0)
    adolecentes_masculinos=models.PositiveBigIntegerField(verbose_name='Adolecentes masculinos',db_column='ADOLECENTES_MASCULINOS',default=0)
    adolecentes_femeninos=models.PositiveBigIntegerField(verbose_name='Adolecentes femeninos',db_column='ADOLECENTES_FEMENINOS',default=0)
    jovenes_masculinos=models.PositiveBigIntegerField(verbose_name='Jovenes masculinos',db_column='JOVENES_MASCULINOS',default=0) 
    jovenes_femeninos=models.PositiveBigIntegerField(verbose_name='Jovenes femeninos',db_column='JOVENES_FEMENINOS',default=0)
    adultos_masculinos=models.PositiveBigIntegerField(verbose_name='Adultos masculinos',db_column='ADULTOS_MASCULINOS',default=0)
    adultos_femeninos=models.PositiveBigIntegerField(verbose_name='Adultos femeninos',db_column='ADULTOS_FEMENINOS',default=0)
    adultos_mayores_masculinos=models.PositiveBigIntegerField(verbose_name='Adultos mayores masculinos',db_column='ADULTOS_MAYORES_MASCULINOS',default=0)
    adultos_mayores_femeninos=models.PositiveBigIntegerField(verbose_name='Adultos mayores femeninos',db_column='ADULTOS_MAYORES_FEMENINOS',default=0)
    xinca=models.PositiveBigIntegerField(verbose_name='Xincas',db_column='XINCAS',default=0)
    garifuna=models.PositiveBigIntegerField(verbose_name='Garifunas',db_column='GARIFUNAS',default=0)
    maya=models.PositiveBigIntegerField(verbose_name='Mayas',db_column='MAYAS',default=0)
    ladino=models.PositiveBigIntegerField(verbose_name='Ladinos',db_column='LADINOS',default=0)

    class Meta:
        db_table='EJE_PREVENCION_RESPUESTA'
        verbose_name='Respuesta de Eje de Prevención'
        verbose_name_plural='Respuestas de Ejes de Prevención'

    def delete(self,*args,**kwargs):
        eliminado=False
        try:
            meta=MetaMensualEP.objects.filter(delegacion=self.delegacion).last()
            if meta:
                print(meta)
                meta.meta_alcanzada-=1
                meta.actualizado=datetime.now()
                meta._NUEVO=True
                meta.save()
                self.meta=meta
            super(EPRespuesta,self).delete(*args,**kwargs)
            eliminado=True
        except:
            print('Algo ha salido mal')
        return eliminado

    def save(self,*args,**kwargs):
        ingresado=False
        try:
            if self._ACTUALIZAR:
                super(EPRespuesta,self).save(*args,**kwargs)
                ingresado=True
            else:
                meta=MetaMensualEP.objects.filter(delegacion=self.delegacion).last()
                if meta:
                    meta.meta_alcanzada+=1
                    meta.actualizado=datetime.now()
                    meta._NUEVO=True
                    meta.save()
                    self.meta=meta
                else:
                    raise ValidationError('No puede responder, aún no tiene una meta asignada')
                super(EPRespuesta,self).save(*args,**kwargs)
                ingresado=True
        except:
            raise ValidationError('Debe completar los campos requeridos')
        return ingresado    

class AORespuesta(models.Model):
    _ACTUALIZAR=False
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    latitud=models.CharField(verbose_name='Latitud',db_column='LATITUD',max_length=25,blank=False,null=False)
    longitud=models.CharField(verbose_name='Longitud',db_column='LONGITUD',max_length=25,blank=False,null=False)
    respondido=models.DateField(verbose_name='Fecha respondido',db_column='FECHA_CREADO',default=timezone.now)
    delegacion=models.ForeignKey(Delegacion,verbose_name='Delegación',db_column='DELEGACION_ID',on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,verbose_name='Usuario',db_column='USUARIO_ID',on_delete=models.CASCADE)
    lugar_priorizado=models.ForeignKey(LugarPriorizado,verbose_name='Lugar priorizado',db_column='PRIORIZADO_ID',on_delete=models.CASCADE)
    lugar_no_priorizado=models.CharField(verbose_name='Lugar no priorizado',db_column='NO_PRIORIZADO',max_length=350)
    lugar_apoyo=models.CharField(verbose_name='Lugar de apoyo',db_column='LUGAR_APOYO',max_length=350)
    plan=models.ForeignKey(PlanArea,verbose_name='Plan/Orden',db_column='PLAN',on_delete=models.CASCADE)
    operativo=models.ForeignKey(TipoOperativo,verbose_name='Tipo de Operativo',db_column='TIPO_OPERATIVO',on_delete=models.CASCADE)
    cantidad=models.PositiveBigIntegerField(verbose_name='Cantidad',db_column='CANTIDAD')
    observaciones=models.TextField(verbose_name='Observaciones',db_column='OBSERVACIONES',max_length=450,blank=True)
    
    total_identificados=models.PositiveBigIntegerField(verbose_name='Total de identificados',db_column='TOTAL_IDENTIFICADOS',default=0)
    hombres_identificados=models.PositiveBigIntegerField(verbose_name='Hombres identificados',db_column='HOMBRES_IDENTIFICADOS',default=0)
    mujeres_identificadas=models.PositiveBigIntegerField(verbose_name='Mujeres identificadas',db_column='MUJERES_IDENTIFICADAS',default=0)
    autos_identificados=models.PositiveBigIntegerField(verbose_name='Autos identificados',db_column='AUTOS_IDENTIFICADOS',default=0)
    motos_identificadas=models.PositiveBigIntegerField(verbose_name='Motos identificadas',db_column='MOTOS_IDENTIFICADAS',default=0)
    armas_identificadas=models.PositiveBigIntegerField(verbose_name='Armas identificadas',db_column='ARMAS_IDENTIFICADAS',default=0) 
    
    total_consignados=models.PositiveBigIntegerField(verbose_name='Total consignados',db_column='TOTA_CONSIGNADOS',default=0)
    hombres_consignados=models.PositiveBigIntegerField(verbose_name='Hombres consignados',db_column='HOMBRES_CONSIGNADOS',default=0)
    mujeres_consignadas=models.PositiveBigIntegerField(verbose_name='Mujeres consignadas',db_column='MUJERES_CONSIGNADAS',default=0)
    autos_consignados=models.PositiveBigIntegerField(verbose_name='Autos consignados',db_column='AUTOS_CONSIGNADOS',default=0)
    motos_consignadas=models.PositiveBigIntegerField(verbose_name='Motos consignadas',db_column='MOTOS_CONSIGNADAS',default=0)
    armas_consignadas=models.PositiveBigIntegerField(verbose_name='Armas consignadas',db_column='ARRMAS_CONSIGNADAS',default=0)
    
    total_conducidos=models.PositiveBigIntegerField(verbose_name='Total conducidos',db_column='TOTAL_CONDUCIDOS',default=0)
    hombres_conducidos=models.PositiveBigIntegerField(verbose_name='Hombres conducidos',db_column='HOMBRES_CONDUCIDOS',default=0)
    mujeres_conducidas=models.PositiveBigIntegerField(verbose_name='Mujeres conducidas',db_column='MUJERES_CONDUCIDAS',default=0)
    
    total_solventes=models.PositiveBigIntegerField(verbose_name='Total solventes',db_column='TOTAL_SOLVENTES',default=0)
    hombres_solventes=models.PositiveBigIntegerField(verbose_name='Hombres solventes',db_column='HOMBRES_SOLVENTES',default=0)
    mujeres_solventes=models.PositiveBigIntegerField(verbose_name='Mujeres solventes',db_column='MUJERES_SOLVENTES',default=0)
    autos_solventes=models.PositiveBigIntegerField(verbose_name='Autos solventes',db_column='AUTOS_SOLVENTES',default=0)
    motos_solventes=models.PositiveBigIntegerField(verbose_name='Motos solventes',db_column='MOTOS_SOLVENTES',default=0)
    armas_solventes=models.PositiveBigIntegerField(verbose_name='Armas solventes',db_column='ARMAS_SOLVENTES',default=0)

    total_recuperados=models.PositiveBigIntegerField(verbose_name='Total recuperados',db_column='TOTAL_RECUPERADOS',default=0)
    autos_recuperados=models.PositiveBigIntegerField(verbose_name='Autos recuperados',db_column='AUTOS_RECUPERADOS',default=0)
    motos_recuperados=models.PositiveBigIntegerField(verbose_name='Motos recuperadas',db_column='MOTOS_RECUPERADAS',default=0)
    armas_recuperados=models.PositiveBigIntegerField(verbose_name='Armas recuperadas',db_column='ARMAS_RECUPERADAS',default=0)
    hombres_recuperados=models.PositiveBigIntegerField(verbose_name='Hombres recuperados',db_column='HOMBRES_RECUPERADOS',default=0)
    mujeres_recuperadas=models.PositiveBigIntegerField(verbose_name='Mujeres recuperadas',db_column='MUJERES_RECUPERADAS',default=0)
    menores_recuperados=models.PositiveBigIntegerField(verbose_name='Menores recuperados',db_column='MENORES_RECUPERADOS',default=0)


    class Meta:
        db_table='AREA_OPERATIVA_RESPUESTA'
        verbose_name='Respuesta de Área Operativa'
        verbose_name_plural='Respuestas de Área Operativa'
    
    def save(self,*args,**kwargs):
        super(AORespuesta,self).save(*args,**kwargs)
        return True