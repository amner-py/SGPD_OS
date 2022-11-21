from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models
from ..operacion.models import Operacion,Plan,EjeTrabajo,Producto,TipoOperativo


class Formulario(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    titulo=models.CharField(verbose_name='Título',db_column='TITULO',max_length=40,blank=False,null=False)
    descripcion=models.CharField(verbose_name='Descripción',db_column='DESCRIPCION',max_length=255,blank=True,null=False)
    creado=models.DateTimeField(verbose_name='Fecha de Creación',db_column='FECHA_CREADO',default=datetime.now,editable=False)
    operacion=models.ForeignKey(Operacion,verbose_name='Operación',db_column='OPERACION_ID',on_delete=models.CASCADE)
    

    class Meta:
        db_table='FORMULARIO'
        verbose_name='FORMULARIO'
        verbose_name_plural='FORMULARIOS'


    def __str__(self):
        return f'{self.titulo}'


class Pregunta(models.Model):
    CAMPO_CHOICE=[
        ('txc','Texto corto'),
        ('txl','Texto largo'),
        ('num','Número'),
        ('rad','Radial'),
        ('cas','Casillas'),
        ('list','Lista'),
    ]
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    enunciado=models.CharField(verbose_name='Enunciado de Pregunta',db_column='ENUNCIADO',max_length=350,blank=False,null=False)
    formulario=models.ForeignKey(Formulario,verbose_name='Formulario',db_column='FORMULARIO_ID',on_delete=models.CASCADE)
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
        try:
            
            pregunta=Pregunta()
            pregunta.formulario=self.formulario
            pregunta.campo='list'
            print(self.pregunta)
            planes=Plan.objects.filter(operacion=self.formulario.operacion)
            ejes=EjeTrabajo.objects.filter(operacion=self.formulario.operacion)
            productos=Producto.objects.filter(operacion=self.formulario.operacion)
            toperativos=TipoOperativo.objects.filter(operacion=self.formulario.operacion)

            hay_plan=len(planes)>0
            hay_eje=len(ejes)>0
            hay_producto=len(productos)>0
            hay_toperativo=len(toperativos)>0
            
            if self.formulario == '---------':
                raise ValidationError('El formulario no puede ir vacío.')

            if hay_plan and (self.pregunta=='plan'):
                enunciado_aux='Plan/Orden'
                pregunta.enunciado=enunciado_aux
                pregunta.save()
                print(pregunta.id)
                for plan in planes:
                    opcion=Opcion()
                    opcion.nombre=plan.nombre
                    opcion.pregunta=Pregunta.objects.get(pk=pregunta.id)
                    opcion.save()
            elif hay_eje and (self.pregunta=='eje'):
                enunciado_aux='Eje de Trabajo'
                pregunta.enunciado=enunciado_aux
                pregunta.save()
                print(pregunta.id)
                for eje in ejes:
                    opcion=Opcion()
                    opcion.nombre=eje.nombre
                    opcion.pregunta=Pregunta.objects.get(pk=pregunta.id)
                    opcion.save()
            elif hay_producto and (self.pregunta=='producto'):
                enunciado_aux='Producto'
                pregunta.enunciado=enunciado_aux
                pregunta.save()
                print(pregunta.id)
                for producto in productos:
                    opcion=Opcion()
                    opcion.nombre=producto.nombre
                    opcion.pregunta=Pregunta.objects.get(pk=pregunta.id)
                    opcion.save()
            elif hay_toperativo and (self.pregunta=='toperativo'):
                enunciado_aux='Tipo de Operativo'
                pregunta.enunciado=enunciado_aux
                pregunta.save()
                print(pregunta.id)
                for toperativo in toperativos:
                    opcion=Opcion()
                    opcion.nombre=toperativo.nombre
                    opcion.pregunta=Pregunta.objects.get(pk=pregunta.id)
                    opcion.save()
            else:
                raise ValidationError('La opcion seleccionada no esta disponible para el formulario')
        except:
            raise ValidationError('Debe completar todos los campos.')
        


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

    def clean(self):
        if self.pregunta.campo != 'list':
            if self.pregunta.campo != 'cas':
                if self.pregunta.campo != 'rad':
                    raise ValidationError('Para crear opciones debe seleccionar una pregunta de tipo: Radial, Casillas o Lista.')
