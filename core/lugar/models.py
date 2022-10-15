from django.db import models
from delegacion.models import Delegacion


class Departamento(models.Model):
    id=models.AutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=40)

    class Meta:
        db_table='DEPARTAMENTO'
        verbose_name='DEPARTAMENTO'
        verbose_name_plural='DEPARTAMENTOS'


    def __str__(self):
        return f'{self.nombre}'


class Municipio(models.Model):
    id=models.AutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=40)
    departamento=models.ForeignKey(Departamento,db_column='DEPARTAMENTO_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='MUNICIPIO'
        verbose_name='MUNICIPIOS'
        verbose_name_plural='MUNICIPIOS'
        
    
    def __str__(self):
        return f'{self.nombre}'


class Lugar(models.Model):
    id=models.AutoField(db_column='ID',primary_key=True)
    direccion=models.CharField(db_column='DIRECCION',max_length=150)
    municipio=models.ForeignKey(Municipio,db_column='MUNICIPIO_ID',on_delete=models.SET_NULL)
    delegacion=models.ForeignKey(Delegacion,db_column='DELEGACION_ID',on_delete=models.SET_NULL)

    
    class Meta:
        db_table='LUGAR'
        verbose_name='LUGAR'
        verbose_name_plural='LUGARES'

    
    def __str__(self):
        return f'{self.direccion}, {self.municipio.nombre}, {self.municipio.departamento.nombre}'