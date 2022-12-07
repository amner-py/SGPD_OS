from django.db import models

class TipoOperativo(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,blank=False,null=False)
    
    class Meta:
        db_table='TIPO_OPERATIVO'
        verbose_name='Tipo de operativo'
        verbose_name_plural='Tipos de operativo'


    def __str__(self):
        return f'{self.nombre}'


class PlanArea(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,null=False,blank=False)

    class Meta:
        db_table='PLAN_AREAOPERATIVA'
        verbose_name='Plan'
        verbose_name_plural='Planes'


    def __str__(self):
        return f'{self.nombre}'