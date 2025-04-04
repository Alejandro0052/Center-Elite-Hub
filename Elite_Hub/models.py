from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Usuario(AbstractUser):
    numero_telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True, blank=True, default=18)
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Nutricionista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)
    especialidad = models.CharField(max_length=115,null=True, blank=True)
    nivel_estudios = models.TextField(max_length=15, null=False)


    def __str__(self):
        return f'{self.usuario}'


class Parametros(models.Model):
      quienes_somos = models.TextField(max_length=900, null=True, blank=True)
      politica_tratamiento_datos = models.TextField(max_length=600, null=True, blank=True)
      contactenos = models.CharField(max_length=255, null=True, blank=True)
      terminos_condiciones = models.TextField(max_length=600, null=True, blank=True)

      #class Meta:
          #verbose_name = 'Parametro'
         # verbose_name_plural = 'Parametros'
        #  ordering = ['orden']

      def __str__(self):
        return f'{self.quienes_somos} - {self.contactenos}'


#EL DEPORTISTA DEBE RELACIONARSE A UN DEPORTE, NO UN DEPORTE A UN DEPORTISTA
class Deportista(models.Model):
    Deporte = [
    ('ciclismo','Ciclismo'),
    ('futbol','Futbol'),
    ('running','Running'),
    ('natacion','Natacion'),
    ]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=20, choices=Deporte)
    descripcion = models.CharField(max_length=50)
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.usuario}'
    
class Patrocinador(models.Model):
    Deportistas_Interes = [
    ('ciclistas','Ciclistas'),
    ('futbolistas','Futbolistas'),
    ('corredores','Corredores'),
    ('nadadores','Nadadores'),
    ]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deportistas_interes = models.CharField(max_length=100, choices=Deportistas_Interes, null=True)
    imagen_de_perfil = models.ImageField(upload_to='patrocinadores/', blank=True, null=True)
    descripcion = models.TextField()
    def __str__(self):
        return f'{self.usuario}' 
    
class Marca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=60, default='Coloca el nombre de tu empresa')
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.usuario}'

class Pqrs(models.Model):
    TIPO = [
        ('peticion','Peticion'),
        ('queja','Queja'),
        ('reclamo','Reclamo'),
        ('sugerencia','Sugerencia'),
        ('demanda','Demanda'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=120, choices=TIPO)
    asunto = models.CharField(max_length=1130)
    descripcion = models.CharField(max_length=255)
    imagen_de_evidencia = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)
    def __str__(self):
       return f'{self.usuario} - {self.asunto}' 

#EL DEPORTISTA DEBE RELACIONARSE A UN DEPORTE, NO UN DEPORTE A UN DEPORTISTA
class Deporte(models.Model):
    Deporte = [
    ('ciclismo','Ciclismo'),
    ('futbol','Futbol'),
    ('running','Running'),
    ('natacion','Natacion'),
    ]
    deportista = models.OneToOneField(Deportista, related_name='deporte_detail',  on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=20, choices=Deporte)
    descripcion = models.TextField()
    imagen_repre_deporte = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
       return f'{self.deportista}'

class Contenido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    contenido_imagen = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
       return f'{self.titulo}'
    

##Another superclass, it is not yet related to more classes, (they are only related to those below)

class Facturacion(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    numero_factura = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    Valor_factura = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre_usuario}'

class EncabezadoFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    resolucion_fact = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'

class DetalleFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_usuario = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'

class Pagos(models.Model): 
      facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
      valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
      fecha_pago =  models.DateField()
      nombre_usuario = models.CharField(max_length=30)

      def __str__(self):
        return f'{self.nombre_usuario}'

