# Generated by Django 4.2.16 on 2024-10-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_Hub', '0008_nutricionista_especialidad_alter_deportista_deporte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='nombre_deporte',
        ),
        migrations.AddField(
            model_name='deporte',
            name='deporte',
            field=models.CharField(choices=[('ciclismo', 'Ciclismo'), ('futbol', 'Futbol'), ('running', 'Running'), ('natacion', 'Natacion')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
