from tabnanny import verbose
from unicodedata import name
from django.db import models


class Departamento(models.Model):
    id=models.AutoField(db_column='ID')
    nombre=models.CharField(db_column='NOMBRE',max_length=30)

    class Meta:
        db_table='DEPARTAMENTO'
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'


class Municipio():
    id=models.AutoField(db_column='ID')
    nombre=models.CharField(db_column='NOMBRE',max_length=40)
    departamento=models.ForeignKey(Departamento,db_column='DEPARTAMENTO_ID',on_delete=models.SET_NULL)

    class Meta:
        db_table='MUNICIPIO'
        verbose_name='Municipio'
        verbose_name_plural='Municipios'


class Estado():
    id=models.AutoField(db_column='ID')
    estado=models.CharField(db_column='ESTADO',max_length=25)

    class Meta:
        db_table='ESTADO'
        verbose_name='Estado'
        verbose_name_plural='Estados'

class Lugar():
    id=models.AutoField(db_column='ID')
    direccion=models.CharField(db_column='DIRECCION',max_length=150)