# Generated by Django 4.1.2 on 2022-11-10 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'OPERACION',
                'verbose_name_plural': 'OPERACIONES',
                'db_table': 'OPERACION',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
                ('operacion', models.ForeignKey(db_column='OPERACION_ID', on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion', verbose_name='Operación')),
            ],
            options={
                'verbose_name': 'PRODUCTO',
                'verbose_name_plural': 'PRODUCTOS',
                'db_table': 'PRODUCTO',
            },
        ),
        migrations.CreateModel(
            name='TipoOperativo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
                ('operacion', models.ForeignKey(db_column='OPERACION_ID', on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion', verbose_name='Operación')),
            ],
            options={
                'verbose_name': 'TIPO DE OPERATIVO',
                'verbose_name_plural': 'TIPOS DE OPERATIVO',
                'db_table': 'TIPO_OPERATIVO',
            },
        ),
        migrations.CreateModel(
            name='Subproducto',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
                ('producto', models.ForeignKey(db_column='PRODUCTO_ID', on_delete=django.db.models.deletion.CASCADE, to='operacion.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'SUBPRODUCTO',
                'verbose_name_plural': 'SUBPRODUCTOS',
                'db_table': 'SUBPRODUCTO',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
                ('operacion', models.ForeignKey(db_column='OPERACION_ID', on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion', verbose_name='Operación')),
            ],
            options={
                'verbose_name': 'PLAN',
                'verbose_name_plural': 'PLANES',
                'db_table': 'PLAN',
            },
        ),
        migrations.CreateModel(
            name='EjeTrabajo',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=350, verbose_name='Nombre')),
                ('operacion', models.ForeignKey(db_column='OPERACION_ID', on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion', verbose_name='Operación')),
            ],
            options={
                'verbose_name': 'EJE DE TRABAJO',
                'verbose_name_plural': 'EJES DE TRABAJO',
                'db_table': 'EJE_TRABAJO',
            },
        ),
    ]
