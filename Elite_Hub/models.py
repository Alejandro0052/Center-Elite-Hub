from django.utils import timezone
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
    descripcion = models.CharField(max_length=50,null=False, blank=False)
    especialidad = models.CharField(max_length=115,null=True, blank=True)
    nivel_estudios = models.TextField(max_length=15, null=False)
    fecha = models.DateTimeField(auto_now_add=True)



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
      
#Api de noticias que debe llevar foto, titulo, texto y fecha

class Noticias(models.Model):
      foto_noticia = models.ImageField(upload_to='noticias/', null=True, blank=True)
      titulo = models.CharField(max_length=30, null=False,blank=True) 
      texto_noticia = models.TextField(max_length=300,null=False, blank=True)
      fecha = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return f'{self.titulo} - {self.texto_noticia}'





    

    


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
    descripcion = models.CharField(max_length=50,null=False, blank=False)
    fecha = models.DateTimeField(default=timezone.now)
    imagen_de_perfil = models.ImageField(upload_to='deportistas/', null=True, blank=True)

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
    #fecha = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(default=timezone.now)
    imagen_de_perfil = models.ImageField(upload_to='patrocinadores/', blank=True, null=True)
    descripcion = models.TextField(max_length=255,null=False, blank=False)
    def __str__(self):
        return f'{self.usuario}' 
    
class Marca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=60, default='Coloca el nombre de tu empresa')
    fecha = models.DateTimeField(default=timezone.now)
    imagen_de_perfil = models.ImageField(upload_to='marcas/', null=True, blank=True)
    descripcion = models.TextField(null=False, blank=False)


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
    #fecha = models.DateTimeField(auto_now_add=True)   
    fecha = models.DateTimeField(default=timezone.now)
    imagen_de_evidencia = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)
    
    def __str__(self):
       return f'{self.usuario} - {self.asunto}' 

#EL DEPORTISTA DEBE RELACIONARSE A UN DEPORTE, NO UN DEPORTE A UN DEPORTISTA
#DE MOMENTO NO SE ESTA USANDO ESTE MODELO
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
#DE MOMENTO NO SE ESTA USANDO ESTE MODELO DEPORTE
 
#Validar donde se esta usando el modelo contenido
class Contenido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    contenido_imagen = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
       return f'{self.titulo}'
    

class Eventos(models.Model):
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    evento_imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)

    def __str__(self):
       return f'{self.titulo}'
    
class Testimonios(models.Model):
    titulo = models.CharField(max_length=55, null=False, blank=False)
    descripcion= models.TextField(max_length=255, null=False, blank=False)
    testimonio_imagen = models.ImageField(upload_to='testimionios', null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.titulo}'
#usuario con foreignkey a usuario
#texto imagen video y fecha de creación

class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='publicaciones')
    texto = models.TextField(max_length=500, null=True, blank=True, verbose_name="Escribe algo!")
    imagen =  models.ImageField(upload_to='publicaciones', null=True, blank=True)
    #agregar un campo de video
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username} - {self.texto[:30]}'




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

