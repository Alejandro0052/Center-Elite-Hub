from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario, Deporte, Deportista, Pqrs, Patrocinador, Contenido, Nutricionista, Marca , Parametros
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class UsuarioCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil') 

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UsuarioChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

    def clean_password(self):
        return self.initial["password"]


def obtener_tipo_usuario(usuario):
    if hasattr(usuario, 'deportista'):
        return "Deportista"
    elif hasattr(usuario, 'patrocinador'):
        return "Patrocinador"
    elif hasattr(usuario, 'marca'):
        return "Marca"
    elif hasattr(usuario, 'nutricionista'):
        return "Nutricionista"
    return "Sin Asignar"

def generar_reporte_pdf_tipos(modeladmin, request, queryset):
    # Crea la respuesta HTTP para descargar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_usuarios_tipos.pdf"'

    # Crea el objeto Canvas para el PDF
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Título del reporte
    p.drawString(100, height - 50, "Reporte de Usuarios por Tipo")

    # Contadores de usuarios por tipo
    total_deportistas = Deportista.objects.count()
    total_patrocinadores = Patrocinador.objects.count()
    total_marcas = Marca.objects.count()
    total_nutricionistas = Nutricionista.objects.count()

    # Imprime los conteos de usuarios en el PDF
    p.drawString(100, height - 100, f"Total de Deportistas: {total_deportistas}")
    p.drawString(100, height - 120, f"Total de Patrocinadores: {total_patrocinadores}")
    p.drawString(100, height - 140, f"Total de Marcas: {total_marcas}")
    p.drawString(100, height - 160, f"Total de Nutricionistas: {total_nutricionistas}")

    # Agrega una línea divisoria
    p.line(100, height - 170, width - 100, height - 170)

    # Agrega los detalles de cada usuario seleccionado
    y_position = height - 190
    for usuario in queryset:
        tipo_usuario = obtener_tipo_usuario(usuario)
        p.drawString(100, y_position, f"Usuario: {usuario.username} - Tipo: {tipo_usuario}")
        y_position -= 20
        if y_position < 50:
            p.showPage()  # Nueva página si se agota el espacio
            y_position = height - 50

    # Cierra el PDF
    p.save()
    return response

generar_reporte_pdf_tipos.short_description = "Generar reporte PDF de usuarios por tipo"

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}), 
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),  # Incluimos los campos personalizados y permisos
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions') 
    actions = [generar_reporte_pdf_tipos]


admin.site.register(Usuario, UsuarioAdmin)
# admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)
admin.site.register(Pqrs)
admin.site.register(Contenido)
admin.site.register(Parametros)
