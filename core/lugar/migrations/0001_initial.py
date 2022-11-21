# Generated by Django 4.1.2 on 2022-11-21 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=40, verbose_name='Nombre')),
                ('path', models.TextField(db_column='PATH', max_length=30000, verbose_name='Path')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'DEPARTAMENTO',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=40, verbose_name='Nombre')),
                ('departamento', models.ForeignKey(db_column='DEPARTAMENTO_ID', on_delete=django.db.models.deletion.CASCADE, to='lugar.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'db_table': 'MUNICIPIO',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='Id')),
                ('direccion', models.CharField(db_column='DIRECCION', max_length=150, verbose_name='Dirección')),
                ('municipio', models.ForeignKey(db_column='MUNICIPIO_ID', on_delete=django.db.models.deletion.CASCADE, to='lugar.municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'db_table': 'LUGAR',
            },
        ),
    ]
