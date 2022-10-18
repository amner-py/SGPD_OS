from django.db import models


class SeccionInicio(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    titulo=models.CharField(db_column='TITULO',max_length=50,blank=False,null=False)
    informacion=models.CharField(db_column='INFORMACION',max_length=350,blank=False,null=False)

    
    class Meta:
        db_table='SECCION_INICIO'
        verbose_name='SECCION INICIO'
        verbose_name_plural='SECCIONES INICIO'

    
    def __str__(self):
        return f'{self.titulo}'


class ImgInicio(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    src=models.ImageField(db_column='SRC',upload_to='carrusel_seccion',null=True)
    seccion=models.ForeignKey(SeccionInicio,db_column='SECCION_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='IMG_INICIO'
        verbose_name='IMAGEN INICIO'
        verbose_name_plural='IMAGENES INCIO'


    def __str__(self):
        return f'{self.src}'


class RedSocial(models.Model):
    id=models.BigAutoField(db_column='ID',primary_key=True)
    nombre=models.CharField(db_column='NOMBRE',max_length=15,blank=False,null=False)
    url=models.CharField(db_column='URL',max_length=350,blank=False,null=False)
    icono=models.ImageField(db_column='ICONO',upload_to='social',null=False)

    
    class Meta:
        db_table='RED_SOCIAL'
        verbose_name='RED SOCIAL'
        verbose_name_plural='REDES SOCIALES'

    def __str__(self):
        return f'{self.nombre.upper}:{self.url}'