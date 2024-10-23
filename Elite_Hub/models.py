from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=80, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=100)
    edad = models.IntegerField()
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'



class Nutricionista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    

   
    def __str__(self):
        return f'{self.usuario}'


class Deportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.usuario.nombre}'

from django.contrib.auth.models import AbstractUser

# class Usuario(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     numero_telefono = models.CharField(max_length=15)
#     correo = models.EmailField(max_length=80, unique=True)
#     fecha_registro = models.DateField(auto_now_add=True)
#     direccion = models.CharField(max_length=100)
#     edad = models.IntegerField()
#     imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

#     def __str__(self):
#         return f'{self.nombre} - {self.apellido}'

class Usuario(AbstractUser):
    numero_telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True, blank=True, default=18)
    imagen_de_perfil = models.ImageField(upload_to='perfil_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Nutricionista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.usuario}'

class Deportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deporte = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.usuario}'
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
    
class Patrocinador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    deportistas_interes = models.CharField(max_length=100)

<<<<<<< HEAD

    def __str__(self):
        return f'{self.usuario}' 
    
    
=======
    def __str__(self):
        return f'{self.usuario}' 
    
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
class Marca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=60, default='Coloca el nombre de tu empresa')

    def __str__(self):
        return f'{self.usuario}'

<<<<<<< HEAD

#class Invitados(models.Model):
  # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
 #   usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
  #  descripcion = models.CharField(max_length=50)
   # nombre = models.CharField(max_length=50)
    #apellido = models.CharField(max_length=50)
    #numero_telefono = models.IntegerField()

    #def __str__(self):
     #   return f'{self.nombre} - {self.descripcion}'


=======
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
class Pqrs(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
       return f'{self.usuario} - {self.asunto}' 

<<<<<<< HEAD

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    #deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    #patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario}' - {self.texto}

#Agregue related_name='deporte_detail'
class Deporte(models.Model):
    deportista = models.OneToOneField(Deportista, related_name='deporte_detail',  on_delete=models.CASCADE, primary_key=True)
    #nombre = models.CharField(max_length=50)
    #descripcion = models.TextField()
=======
#Agregue related_name='deporte_detail'
class Deporte(models.Model):
    deportista = models.OneToOneField(Deportista, related_name='deporte_detail',  on_delete=models.CASCADE, primary_key=True)
    descripcion = models.TextField()
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927

    def __str__(self):
       return f'{self.deportista}'

<<<<<<< HEAD

class Contenido(models.Model):
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    #deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
   # patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
=======
class Contenido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=55)
    descripcion = models.TextField()
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927

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

<<<<<<< HEAD


=======
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
class EncabezadoFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    resolucion_fact = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'

<<<<<<< HEAD

=======
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
class DetalleFact(models.Model):
    facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_usuario = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre_usuario}'

<<<<<<< HEAD

=======
>>>>>>> b61cb2f1500eee577051c0e31a95bb311c5e6927
class Pagos(models.Model): 
      facturacion = models.OneToOneField(Facturacion, on_delete=models.CASCADE, primary_key=True)
      valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
      fecha_pago =  models.DateField()
      nombre_usuario = models.CharField(max_length=30)

      def __str__(self):
        return f'{self.nombre_usuario}'