# Generated by Django 4.1.2 on 2024-06-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id_nav', models.AutoField(db_column='idNav', primary_key=True, serialize=False)),
                ('nombre_nav', models.CharField(max_length=20)),
                ('url_nav', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Navs',
            },
        ),
    ]
