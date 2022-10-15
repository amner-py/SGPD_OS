from django.db import models


class Formulario(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    titulo=models.CharField(db_column='TITULO',max_length=40,blank=False,null=False)