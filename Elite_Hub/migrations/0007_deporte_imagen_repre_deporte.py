# Generated by Django 4.2.16 on 2024-10-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_Hub', '0006_deportista_imagen_de_perfil_marca_imagen_de_perfil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deporte',
            name='imagen_repre_deporte',
            field=models.ImageField(blank=True, null=True, upload_to='perfil_imagenes/'),
        ),
    ]
