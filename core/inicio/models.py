from django.db import models
from tinymce import models as TinyMCE


class SeccionInicio(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    titulo=models.CharField(verbose_name='Título',db_column='TITULO',max_length=50,blank=False,null=False)
    informacion=TinyMCE.HTMLField(verbose_name='Información',db_column='INFORMACION',max_length=3000,blank=False,null=False)

    
    class Meta:
        db_table='SECCION_INICIO'
        verbose_name='Sección de inicio'
        verbose_name_plural='Secciones de inicio'

    
    def __str__(self):
        return f'{self.titulo}'


class ImgInicio(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    src=models.ImageField(verbose_name='Ruta',db_column='SRC',upload_to='carrusel_seccion',null=True)
    seccion=models.ForeignKey(SeccionInicio,verbose_name='Sección',db_column='SECCION_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='IMG_INICIO'
        verbose_name='Imagen de inicio'
        verbose_name_plural='Imágenes de inicio'


    def __str__(self):
        return f'{self.src}'
    
    def delete(self):
        self.src.delete(save=False)
        return super().delete()

    def save(self, *args, **kwargs):
     try:
      previous = ImgInicio.objects.get(id=self.id)
      if previous.src != self.src:
       previous.src.delete(save=False)
     except: pass
     super(ImgInicio, self).save(*args, **kwargs)

class RedSocial(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=15,blank=False,null=False)
    url=models.CharField(verbose_name='Enlace URL',db_column='URL',max_length=350,blank=False,null=False)
    icono=models.ImageField(verbose_name='Icono',db_column='ICONO',upload_to='social',null=False)

    
    class Meta:
        db_table='RED_SOCIAL'
        verbose_name='Red social'
        verbose_name_plural='Redes sociales'

    def __str__(self):
        return f'{self.nombre}: {self.url}'
    
    def delete(self):
        self.icono.delete(save=False)
        return super().delete()

    def save(self, *args, **kwargs):
     try:
      previous = RedSocial.objects.get(id=self.id)
      if previous.icono != self.icono:
       previous.icono.delete(save=False)
     except: pass
     super(RedSocial, self).save(*args, **kwargs)