# Generated by Django 4.2.16 on 2024-11-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_Hub', '0016_rename_conntactenos_parametros_contactenos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='tipo',
            field=models.CharField(choices=[('peticion', 'Peticion'), ('queja', 'Queja'), ('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia'), ('demanda', 'Demanda')], max_length=20),
        ),
    ]
