# Generated by Django 4.1.2 on 2022-10-27 11:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lugar', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(db_column='FECHA', default=datetime.datetime.now, editable=False, verbose_name='Fecha')),
                ('delegacion', models.OneToOneField(db_column='DELEGACION_ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Delegación')),
                ('lugar', models.OneToOneField(db_column='LUGAR_ID', on_delete=django.db.models.deletion.CASCADE, to='lugar.lugar', verbose_name='Lugar')),
            ],
            options={
                'verbose_name': 'ASIGNACION',
                'verbose_name_plural': 'ASIGNACIONES',
                'db_table': 'ASIGNACION',
            },
        ),
    ]
