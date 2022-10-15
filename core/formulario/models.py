from datetime import datetime
from django.db import models
from core.operacion.models import Plan


class Formulario(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    titulo=models.CharField(db_column='TITULO',max_length=40,blank=False,null=False)
    descripcion=models.CharField(db_column='DESCRIPCION',max_length=255,blank=True,null=False)
    creado=models.DateTimeField(db_column='FECHA_CREADO',default=datetime.now,editable=False)
    plan=models.ForeignKey(Plan,db_column='PLAN_ID',on_delete=models.CASCADE)
    

    class Meta:
        db_table='FORMULARIO'
        verbose_name='FORMULARIO'
        verbose_name_plural='FORMULARIOS'


    def __str__(self):
        return f'{self.titulo}'


class Seccion(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    titulo=models.CharField(db_column='TITULO',max_length=40)
    formulario=models.ForeignKey(Formulario,db_column='FORMULARIO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='SECCION_FORMULARIO'
        verbose_name='SECCION DE FORMULARIO'
        verbose_name_plural='SECCIONES DE FORMULARIO'

    
    def __str__(self):
        return f'{self.titulo}'


class TipoCampo(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=20)

    
    class Meta:
        db_table='TIPO_CAMPO'
        verbose_name='TIPO DE CAMPO'
        verbose_name_plural='TIPOS DE CAMPO'


    def __str__(self):
        return f'{self.nombre}'


class Pregunta(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    enunciado=models.CharField(db_column='ENUNCIADO',max_length=350,blank=False,null=False)
    formulario=models.ForeignKey(Formulario,db_column='FORMULARIO_ID',on_delete=models.CASCADE)
    seccion=models.ForeignKey(Seccion,db_column='SECCION_ID',on_delete=models.SET_NULL)
    campo=models.ForeignKey(TipoCampo,db_column='TIPOC_ID',on_delete=models.SET_NULL)


    class Meta:
        db_table='PREGUNTA'
        verbose_name='PREGUNTA'
        verbose_name_plural='PREGUNTAS'

    
    def __str__(self):
        return f'{self.enunciado}'