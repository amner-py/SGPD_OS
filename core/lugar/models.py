from django.db import models
from tinymce import models as TinyMCE


class Departamento(models.Model):
    id=models.AutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=40,null=False,blank=False)
    path=models.TextField(verbose_name='Path',db_column='PATH',max_length=30000,blank=True)

    class Meta:
        db_table='DEPARTAMENTO'
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'


    def __str__(self):
        return f'{self.nombre}'


class Municipio(models.Model):
    id=models.AutoField(verbose_name='Id',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=40,null=False,blank=False)
    departamento=models.ForeignKey(Departamento,verbose_name='Departamento',db_column='DEPARTAMENTO_ID',on_delete=models.CASCADE)
    path=models.TextField(verbose_name='Path',db_column='PATH',max_length=30000,blank=True)

    class Meta:
        db_table='MUNICIPIO'
        verbose_name='Municipio'
        verbose_name_plural='Municipios'
        
    
    def __str__(self):
        return f'{self.nombre}'


class Lugar(models.Model):
    id=models.AutoField(verbose_name='Id',db_column='ID',primary_key=True)
    direccion=models.CharField(verbose_name='Dirección',db_column='DIRECCION',max_length=150,null=False,blank=True)
    municipio=models.ForeignKey(Municipio,verbose_name='Municipio',db_column='MUNICIPIO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='LUGAR'
        verbose_name='Lugar'
        verbose_name_plural='Lugares'

    
    def __str__(self):
        if self.direccion:
            return f'{self.direccion}, {self.municipio.nombre}, {self.municipio.departamento.nombre}'
        else:
            return f'{self.municipio.nombre}, {self.municipio.departamento.nombre}'