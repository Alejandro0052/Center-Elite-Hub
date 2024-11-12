from django.contrib import admin

from Elite_Hub.models import Usuario,Deporte,Deportista,Nutricionista, Patrocinador, Marca, Contenido
 
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'numero_telefono', 'correo']
    list_display_links = ['nombre']  # Permitir click en el nombre para ver el detalle
 #   readonly_fields = ['nombre', 'apellido', 'numero_telefono', 'correo',]








admin.site.register(Usuario,  UsuarioAdmin)
admin.site.register(Deporte)
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario, Deporte, Deportista, Pqrs, Patrocinador, Contenido, Nutricionista, Marca , Parametros
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openpyxl import Workbook
from io import BytesIO
import tempfile
import matplotlib
matplotlib.use('Agg')  # Usar el backend Agg (sin GUI)
import matplotlib.pyplot as plt

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
    # Obtener datos para el gráfico
    total_deportistas = Deportista.objects.count()
    total_patrocinadores = Patrocinador.objects.count()
    total_marcas = Marca.objects.count()
    total_nutricionistas = Nutricionista.objects.count()
    total_sin_asignar = sum(1 for usuario in queryset if obtener_tipo_usuario(usuario) == "Sin Asignar")

    labels = ['Deportistas', 'Patrocinadores', 'Marcas', 'Nutricionistas', 'Sin Asignar']
    sizes = [total_deportistas, total_patrocinadores, total_marcas, total_nutricionistas, total_sin_asignar]

    # Crear el gráfico circular
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')

    # Guardar el gráfico en un archivo temporal
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        plt.savefig(tmp_file.name, format='png')
        plt.close()

        # Generar el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_usuarios_tipos.pdf"'
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        p.drawString(100, height - 50, "Reporte de Usuarios")
        p.drawString(100, height - 100, f"Total de Deportistas: {total_deportistas}")
        p.drawString(100, height - 120, f"Total de Patrocinadores: {total_patrocinadores}")
        p.drawString(100, height - 140, f"Total de Marcas: {total_marcas}")
        p.drawString(100, height - 160, f"Total de Nutricionistas: {total_nutricionistas}")
     #   p.drawString(100, height - 180, f"Total de Usuarios Sin Asignar: {total_sin_asignar}")

        # Insertar el gráfico en el PDF
        p.drawImage(tmp_file.name, 150, height - 450, width=300, height=300)

        p.save()
        plt.close()

    return response
generar_reporte_pdf_tipos.short_description = "Generar reporte PDF de usuarios por tipo"


def generar_reporte_excel_tipos(modeladmin, request, queryset):
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Usuarios"

    
    ws.append(["Usuario", "Tipo"])

    # Contar los totales de cada tipo de usuario
    total_deportistas = Deportista.objects.count()
    total_patrocinadores = Patrocinador.objects.count()
    total_marcas = Marca.objects.count()
    total_nutricionistas = Nutricionista.objects.count()
    total_usuarios = queryset.count()
   # total_sin_asignar = sum(1 for usuario in queryset if obtener_tipo_usuario(usuario) == "Sin Asignar")

    # Escribir los totales en el archivo Excel
    ws.append([])
    ws.append(["Total de Deportistas", total_deportistas])
    ws.append(["Total de Patrocinadores", total_patrocinadores])
    ws.append(["Total de Marcas", total_marcas])
    ws.append(["Total de Nutricionistas", total_nutricionistas])
 #   ws.append(["Total de Usuarios Sin Asignar", total_sin_asignar])
    ws.append(["Total de Usuarios", total_usuarios])


    ws.append([])


    for usuario in queryset:
        tipo_usuario = obtener_tipo_usuario(usuario)
        ws.append([usuario.username, tipo_usuario])


    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename="reporte_usuarios_tipos.xlsx"'
    

    wb.save(response)
    return response

generar_reporte_excel_tipos.short_description = "Generar reporte Excel de usuarios por tipo"

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}), 
    )
    #, 'user_permissions
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups'),  # , 'user_permissions'
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions') 
    actions = [generar_reporte_pdf_tipos,generar_reporte_excel_tipos]



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)
admin.site.register(Pqrs)
admin.site.register(Contenido)
admin.site.register(Parametros)
