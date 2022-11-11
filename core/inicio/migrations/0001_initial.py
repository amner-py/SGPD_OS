# Generated by Django 4.1.2 on 2022-11-10 23:02

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=15, verbose_name='Nombre')),
                ('url', models.CharField(db_column='URL', max_length=350, verbose_name='Enlace URL')),
                ('icono', models.ImageField(db_column='ICONO', upload_to='social', verbose_name='Icono')),
            ],
            options={
                'verbose_name': 'RED SOCIAL',
                'verbose_name_plural': 'REDES SOCIALES',
                'db_table': 'RED_SOCIAL',
            },
        ),
        migrations.CreateModel(
            name='SeccionInicio',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_column='TITULO', max_length=50, verbose_name='Título')),
                ('informacion', tinymce.models.HTMLField(db_column='INFORMACION', max_length=3000, verbose_name='Información')),
            ],
            options={
                'verbose_name': 'SECCION INICIO',
                'verbose_name_plural': 'SECCIONES INICIO',
                'db_table': 'SECCION_INICIO',
            },
        ),
        migrations.CreateModel(
            name='ImgInicio',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(db_column='SRC', null=True, upload_to='carrusel_seccion', verbose_name='Ruta')),
                ('seccion', models.ForeignKey(db_column='SECCION_ID', on_delete=django.db.models.deletion.CASCADE, to='inicio.seccioninicio', verbose_name='Sección')),
            ],
            options={
                'verbose_name': 'IMAGEN INICIO',
                'verbose_name_plural': 'IMAGENES INCIO',
                'db_table': 'IMG_INICIO',
            },
        ),
    ]
