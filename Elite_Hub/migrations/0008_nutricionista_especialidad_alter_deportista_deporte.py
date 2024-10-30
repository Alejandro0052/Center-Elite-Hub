# Generated by Django 4.2.16 on 2024-10-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_Hub', '0007_deporte_imagen_repre_deporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutricionista',
            name='especialidad',
            field=models.CharField(blank=True, max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='deportista',
            name='deporte',
            field=models.CharField(choices=[('ciclismo', 'Ciclismo'), ('futbol', 'Futbol'), ('running', 'Running'), ('natacion', 'Natacion')], max_length=20),
        ),
    ]
