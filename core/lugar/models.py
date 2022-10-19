from django.db import models


class Departamento(models.Model):
    id=models.AutoField(verbose_name='ID',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=40,null=False,blank=False)

    class Meta:
        db_table='DEPARTAMENTO'
        verbose_name='DEPARTAMENTO'
        verbose_name_plural='DEPARTAMENTOS'


    def __str__(self):
        return f'{self.nombre}'


class Municipio(models.Model):
    id=models.AutoField(verbose_name='ID',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=40,null=False,blank=False)
    departamento=models.ForeignKey(Departamento,verbose_name='Departamento',db_column='DEPARTAMENTO_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='MUNICIPIO'
        verbose_name='MUNICIPIOS'
        verbose_name_plural='MUNICIPIOS'
        
    
    def __str__(self):
        return f'{self.nombre}'


class Lugar(models.Model):
    id=models.AutoField(verbose_name='ID',db_column='ID',primary_key=True)
    direccion=models.CharField(verbose_name='Dirección',db_column='DIRECCION',max_length=150,null=False,blank=False)
    municipio=models.ForeignKey(Municipio,verbose_name='Municipio',db_column='MUNICIPIO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='LUGAR'
        verbose_name='LUGAR'
        verbose_name_plural='LUGARES'

    
    def __str__(self):
        return f'{self.direccion}, {self.municipio.nombre}, {self.municipio.departamento.nombre}'