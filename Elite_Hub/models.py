from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    # Agrega campos adicionales si es necesario
    perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='elitehub_usuario_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='elitehub_usuario_permissions')



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='publicaciones/', null=True, blank=True)

   
    
    

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion}"




class PQRS(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} - {self.usuario.username}"


