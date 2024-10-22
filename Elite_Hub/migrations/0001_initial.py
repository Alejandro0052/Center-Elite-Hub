# Generated by Django 4.2.16 on 2024-10-22 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('deporte', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('numero_factura', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('Valor_factura', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nutricionista',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('deportistas_interes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('deportista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='deporte_detail', serialize=False, to='Elite_Hub.deportista')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFact',
            fields=[
                ('facturacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Elite_Hub.facturacion')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_usuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EncabezadoFact',
            fields=[
                ('facturacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Elite_Hub.facturacion')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('resolucion_fact', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('facturacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Elite_Hub.facturacion')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('nombre_usuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numero_telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=80, unique=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('imagen_de_perfil', models.ImageField(blank=True, null=True, upload_to='perfil_imagenes/')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(default='Coloca el nombre de tu empresa', max_length=60)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=55)),
                ('descripcion', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
