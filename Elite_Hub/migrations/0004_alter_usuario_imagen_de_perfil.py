# Generated by Django 4.2.16 on 2024-10-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_Hub', '0003_remove_comentarios_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil_imagenes/'),
        ),
    ]