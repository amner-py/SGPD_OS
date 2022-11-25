from django.db import models


class Operacion(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,blank=False,null=False)
    
    class Meta:
        db_table='OPERACION'
        verbose_name='Operación'
        verbose_name_plural='Operaciones'


    def __str__(self):
        return f'{self.nombre}'

class TipoOperativo(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,blank=False,null=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='Operaciones',on_delete=models.CASCADE)
    
    class Meta:
        db_table='TIPO_OPERATIVO'
        verbose_name='Tipo de operativo'
        verbose_name_plural='Tipos de operativo'


    def __str__(self):
        return f'{self.nombre}'

    
class EjeTrabajo(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,blank=False,null=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='Operaciones',on_delete=models.CASCADE)
    
    class Meta:
        db_table='EJE_TRABAJO'
        verbose_name='Eje de trabajo'
        verbose_name_plural='Ejes de trabajo'

    
    def __str__(self):
        return f'{self.nombre}'

    
class Producto(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,null=False,blank=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='Operaciones',on_delete=models.CASCADE)
    
    class Meta:
        db_table='PRODUCTO'
        verbose_name='Producto'
        verbose_name_plural='Productos'

    
    def __str__(self):
        return f'{self.nombre}'


class Subproducto(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,null=False,blank=False)
    producto=models.ForeignKey(Producto,verbose_name='Producto',db_column='PRODUCTO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='SUBPRODUCTO'
        verbose_name='Subproducto'
        verbose_name_plural='Subproductos'

    
    def __str__(self):
        return f'{self.nombre}'


class Plan(models.Model):
    id=models.BigAutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=350,null=False,blank=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='Operaciones',on_delete=models.CASCADE)

    class Meta:
        db_table='PLAN'
        verbose_name='Plan'
        verbose_name_plural='Planes'


    def __str__(self):
        return f'{self.nombre}'


