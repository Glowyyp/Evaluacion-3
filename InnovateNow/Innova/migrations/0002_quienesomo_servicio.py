# Generated by Django 4.1.2 on 2024-06-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Innova', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quienesomo',
            fields=[
                ('id_quienesomos', models.AutoField(db_column='idQuienesomos', primary_key=True, serialize=False)),
                ('titulo_quienesomos', models.CharField(max_length=20)),
                ('descripcion_quienesomos', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Quienes_somos',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(db_column='idServicios', primary_key=True, serialize=False)),
                ('titulo_servicio', models.CharField(max_length=20)),
                ('descripcion_servicio', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Servicio',
            },
        ),
    ]
