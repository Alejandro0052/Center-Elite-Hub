from django.contrib import admin
from Elite_Hub.models import Usuario,Deporte,Deportista,Nutricionista, Patrocinador, Marca #, Contenido

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'numero_telefono', 'email']
    list_display_links = ['first_name']  # Permitir click en el nombre para ver el detalle
    # readonly_fields = ['nombre', 'apellido', 'numero_telefono', 'correo',]


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)
#admin.site.register(Contenido)

