from django.db import models


class Operacion(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350)

    
    class Meta:
        db_table='OPERACION'
        verbose_name='OPERACION'
        verbose_name_plural='OPERACIONES'

    
    def __str__(self):
        return f'{self.nombre}'


class TipoOperativo(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350,blank=False,null=False)
    operacion=models.ForeignKey(Operacion,db_column='OPERACION_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='TIPO_OPERATIVO'
        verbose_name='TIPO DE OPERATIVO'
        verbose_name_plural='TIPOS DE OPERATIVO'


    def __str__(self):
        return f'{self.nombre}'

    
class EjeTrabajo(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350,blank=False,null=False)
    operacion=models.ForeignKey(Operacion,db_column='OPERACION_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='EJE_TRABAJO'
        verbose_name='EJE DE TRABAJO'
        verbose_name_plural='EJES DE TRABAJO'

    
    def __str__(self):
        return f'{self.nombre}'

    
class Producto(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350)
    opearcion=models.ForeignKey(Operacion,db_column='OPERACION_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='PRODUCTO'
        verbose_name='PRODUCTO'
        verbose_name_plural='PRODUCTOS'

    
    def __str__(self):
        return f'{self.nombre}'


class Subproducto(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350)
    producto=models.ForeignKey(Producto,db_column='PRODUCTO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='SUBPRODUCTO'
        verbose_name='SUBPRODUCTO'
        verbose_name_plural='SUBPRODUCTOS'

    
    def __str__(self):
        return f'{self.nombre}'


class Plan(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=350)
    operacion=models.ForeignKey(Operacion,db_column='OPERACION_ID',on_delete=models.CASCADE)


    class Meta:
        db_table='PLAN'
        verbose_name='PLAN'
        verbose_name_plural='PLANES'


    def __str__(self):
        return f'{self.nombre}'