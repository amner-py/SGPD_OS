from django.db import models
from delegacion.models import Delegacion


class Notificacion(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    motivo=models.CharField(db_column='MOTIVO',max_length=50)
    mensaje=models.CharField(db_column='MENSAJE')
    emisor=models.ForeignKey(Delegacion,db_column='EMISOR',on_delete=models.CASCADE)
    leido=models.BooleanField(db_column='LEIDO',default=False)