from django.contrib import admin
from .models import Usuario,Deporte,Deportista,Nutricionista, Patrocinador, Marca


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'numero_telefono', 'correo']
    list_display_links = ['nombre']  # Permitir click en el nombre para ver el detalle
 #   readonly_fields = ['nombre', 'apellido', 'numero_telefono', 'correo',]

def has_change_permission(self, request, obj=None):
        return False  # Cambiar a False para  evitar la edición desde aquí





admin.site.register(Usuario,  UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)



   