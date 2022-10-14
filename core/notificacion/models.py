from tabnanny import verbose
from django.db import models
from delegacion.models import Delegacion


class Notificacion(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    motivo=models.CharField(db_column='MOTIVO',max_length=50)
    mensaje=models.CharField(db_column='MENSAJE',max_length=350)
    emisor=models.ForeignKey(Delegacion,db_column='EMISOR',on_delete=models.CASCADE)
    leido=models.BooleanField(db_column='LEIDO',default=False)

    class Meta:
        db_table='NOTIFICACION'
        verbose_name='NOTIFICACION'
        verbose_name_plural='NOTIFICACIONES'


    def __str__(self):
        return f'{self.mensaje} \u1F5F8' if self.leido else f'{self.mensaje}'

class Destinatario(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    usuario=models.ForeignKey(Delegacion,db_column='USUARIO',on_delete=models.SET_NULL)
    notificacion=models.ForeignKey(Notificacion,db_column='NOTIFICACION_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='DESTINATARIO'
        verbose_name='DESTINATARIO'
        verbose_name_plural='DESTINATARIOS'