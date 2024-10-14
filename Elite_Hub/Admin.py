from django.contrib import admin
from .models import Usuario,Deporte,Deportista,Nutricionista, Patrocinador, Marca

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'edad', 'direccion')








admin.site.register(Usuario,  UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)



   