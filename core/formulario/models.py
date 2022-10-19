from datetime import datetime
from django.db import models
from core.operacion.models import Plan


class Formulario(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    titulo=models.CharField(verbose_name='Título',db_column='TITULO',max_length=40,blank=False,null=False)
    descripcion=models.CharField(verbose_name='Descripción',db_column='DESCRIPCION',max_length=255,blank=True,null=False)
    creado=models.DateTimeField(verbose_name='Fecha de Creación',db_column='FECHA_CREADO',default=datetime.now,editable=False)
    plan=models.ForeignKey(Plan,verbose_name='Plan',db_column='PLAN_ID',on_delete=models.CASCADE)
    

    class Meta:
        db_table='FORMULARIO'
        verbose_name='FORMULARIO'
        verbose_name_plural='FORMULARIOS'


    def __str__(self):
        return f'{self.titulo}'


class SeccionFormulario(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    titulo=models.CharField(verbose_name='Título',db_column='TITULO',max_length=40,null=False,blank=False)
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE)

    
    class Meta:
        db_table='SECCION_FORMULARIO'
        verbose_name='SECCION DE FORMULARIO'
        verbose_name_plural='SECCIONES DE FORMULARIO'

    
    def __str__(self):
        return f'{self.titulo}'


class TipoCampo(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=20,null=False,blank=False)

    
    class Meta:
        db_table='TIPO_CAMPO'
        verbose_name='TIPO DE CAMPO'
        verbose_name_plural='TIPOS DE CAMPO'


    def __str__(self):
        return f'{self.nombre}'


class Pregunta(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    enunciado=models.CharField(verbose_name='Enunciado de Pregunta',db_column='ENUNCIADO',max_length=350,blank=False,null=False)
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE)
    seccion=models.ForeignKey(SeccionFormulario,verbose_name='Sección',db_column='SECCION_ID',on_delete=models.CASCADE)
    campo=models.ForeignKey(TipoCampo,verbose_name='Tipo de Campo',db_column='TIPOC_ID',on_delete=models.CASCADE)


    class Meta:
        db_table='PREGUNTA'
        verbose_name='PREGUNTA'
        verbose_name_plural='PREGUNTAS'

    
    def __str__(self):
        return f'{self.enunciado}'