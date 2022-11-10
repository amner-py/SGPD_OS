from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models
from ..operacion.models import Operacion,Plan,EjeTrabajo,Producto,TipoOperativo


class Formulario(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    titulo=models.CharField(verbose_name='Título',db_column='TITULO',max_length=40,blank=False,null=False)
    descripcion=models.CharField(verbose_name='Descripción',db_column='DESCRIPCION',max_length=255,blank=True,null=False)
    creado=models.DateTimeField(verbose_name='Fecha de Creación',db_column='FECHA_CREADO',default=datetime.now,editable=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='PLAN_ID',on_delete=models.CASCADE)
    

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


class Pregunta(models.Model):
    CAMPO_CHOICE=[
        ('txc','Texto corto'),
        ('txl','Texto largo'),
        ('num','Número entero'),
        ('dec','Decimal'),
        ('rad','Radial'),
        ('cas','Casillas'),
        ('list','Lista'),
    ]
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    enunciado=models.CharField(verbose_name='Enunciado de Pregunta',db_column='ENUNCIADO',max_length=350,blank=False,null=False)
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE)
    seccion=models.ForeignKey(SeccionFormulario,verbose_name='Sección',db_column='SECCION_ID',on_delete=models.CASCADE,null=True,blank=True)
    campo=models.CharField(verbose_name='Tipo de campo',db_column='CAMPO',max_length=15,choices=CAMPO_CHOICE)
    

    class Meta:
        db_table='PREGUNTA'
        verbose_name='PREGUNTA'
        verbose_name_plural='PREGUNTAS'

    
    def __str__(self):
        return f'{self.enunciado}'


class PreguntaAuxiliar(models.Model):
    
    PAUX_CHOICE=[
        ('plan','PLAN'),
        ('eje','EJE DE TRABAJO'),
        ('producto','PRODUCTO'),
        ('toperativo','TIPO DE OPERATIVO'),
    ]
    
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE,null=False)
    pregunta=models.CharField(verbose_name='Pregunta',db_column='PREGUNTA',choices=PAUX_CHOICE,max_length=20,unique=True)

    class Meta:
        db_table='PREGUNTA_AUXILIAR'
        verbose_name='PREGUNTA AUXILIAR'
        verbose_name_plural='PREGUNTAS AUXILIARES'

    def __str__(self):
        return f'{self.pregunta}'

    def clean(self):
        plan=len(Plan.objects.filter(operacion=self.formulario.operacion))>0
        eje=len(EjeTrabajo.objects.filter(operacion=self.formulario.operacion))>0
        producto=len(Producto.objects.filter(operacion=self.formulario.operacion))>0
        toperativo=len(TipoOperativo.objects.filter(operacion=self.formulario.operacion))>0

        if self.formulario == '':
            raise ValidationError('El formulario no puede ir vacío.')

        if not plan and self.pregunta=='plan':
            raise ValidationError('Plan no esta disponible para este formulario.')
        else:
            enunciado_aux='Plan'
        if not eje and self.pregunta=='eje':
            raise ValidationError('Eje de Trabajo no esta disponible para este formulario.')
        else:
            enunciado_aux='Eje de Trabajo'
        if not producto and self.pregunta=='producto':
            raise ValidationError('Producto no esta disponible para este formulario.')
        else:
            enunciado_aux='Producto'
        if not toperativo and self.pregunta=='toperativo':
            raise ValidationError('Tipo de Operativo no esta disponible para este formulario.')
        else:
            enunciado_aux='Tipo de Operativo'
        
        Pregunta.objects.create(enunciado=enunciado_aux,formulario=self.formulario,campo='list')


class Validacion(models.Model):
    CONDICION_CHOICE=[
        ('me','Menor que'),
        ('ma','Mayor que'),
        ('mei','Menor o igual que'),
        ('mai','Mayor o igual que'),
        ('i','Igual que'),
    ]

    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    condicion=models.CharField(verbose_name='Condición',db_column='CONDICION',max_length=30,choices=CONDICION_CHOICE)
    numero_a_validar=models.PositiveBigIntegerField(verbose_name='Número a validar',db_column='NUMERO_A_VALIDAR')
    pregunta=models.ForeignKey(Pregunta,verbose_name='Pregunta',db_column='PREGUNTA_ID',on_delete=models.CASCADE)

    class Meta:
        verbose_name='VALIDACION'
        verbose_name_plural='VALIDACIONES'


class Opcion(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',null=False,blank=False,max_length=250)
    pregunta=models.ForeignKey(Pregunta,verbose_name='Pregunta',db_column='PREGUNTA_ID',on_delete=models.CASCADE)


    class Meta:
        db_table='OPCION'
        verbose_name='OPCION'
        verbose_name_plural='OPCIONES'


    def __str__(self):
        return f'{self.nombre}'