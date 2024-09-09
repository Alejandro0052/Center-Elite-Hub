from django.contrib import admin
from .models import Usuario, Categoria, Publicacion, Comentario, PQRS

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(PQRS)
