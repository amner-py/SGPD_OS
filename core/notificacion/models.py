from django.db import models
from ..delegacion.models import Usuario
from datetime import datetime
from tinymce import models as TinyMCE


class Notificacion(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    motivo=models.CharField(verbose_name='Motivo',db_column='MOTIVO',max_length=150,null=False,blank=False,help_text='El motivo tiene como máximo 150 caracteres permitidos')
    mensaje=TinyMCE.HTMLField(verbose_name='Mensaje',db_column='MENSAJE',max_length=350,null=False,blank=False,help_text='El mensaje tiene como máximo 350 caracteres permitidos.')
    receptor=models.ForeignKey(Usuario,verbose_name='Receptor',db_column='RECEPTOR',on_delete=models.CASCADE)
    leido=models.BooleanField(verbose_name='Leído',db_column='LEIDO',default=False)
    fechahora=models.DateTimeField(verbose_name='Feha y Hora',db_column='FECHA_HORA',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='NOTIFICACION'
        verbose_name='Notificación'
        verbose_name_plural='Notificaciones'


    def __str__(self):
        return f'{self.mensaje}'
