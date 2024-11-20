from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario, Deporte, Deportista, Pqrs, Patrocinador, Contenido, Nutricionista, Marca , Parametros
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import tempfile
import matplotlib
matplotlib.use('Agg')  # Usar el backend Agg (sin GUI)
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from django.urls import path



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
    total_deportistas = Deportista.objects.count()
    total_patrocinadores = Patrocinador.objects.count()
    total_marcas = Marca.objects.count()
    total_nutricionistas = Nutricionista.objects.count()
    total_usuarios = Usuario.objects.count()
    total_sin_asignar = sum(1 for usuario in queryset if obtener_tipo_usuario(usuario) == "Sin Asignar")
    
    labels = ['Deportistas', 'Patrocinadores', 'Marcas', 'Nutricionistas', 'Sin Asignar']
    sizes = [total_deportistas, total_patrocinadores, total_marcas, total_nutricionistas, total_sin_asignar]  

  
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')

   
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as pie_chart_file:
        plt.savefig(pie_chart_file.name, format='png')
        plt.close()


    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'])
    plt.xlabel("Tipo de Usuario")
    plt.ylabel("Cantidad")
    plt.title("Cantidad de Usuarios por Tipo")

  
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as bar_chart_file:
        plt.savefig(bar_chart_file.name, format='png')
        plt.close()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_usuarios_tipos.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    y_position = height - 50

    
    p.drawString(100, y_position, "Listado de Usuarios")
    y_position -= 20


    for usuario in queryset:
        tipo_usuario = obtener_tipo_usuario(usuario)
        p.drawString(100, y_position, f"{usuario.first_name} | {usuario.email} | {tipo_usuario}")
        y_position -= 20

       
        if y_position < 100:
            p.showPage()
            y_position = height - 50


    p.drawString(100, y_position, "Resumen de Usuarios")
    y_position -= 30
    p.drawString(100, y_position, f"Total de Deportistas: {total_deportistas}")
    y_position -= 20
    p.drawString(100, y_position, f"Total de Patrocinadores: {total_patrocinadores}")
    y_position -= 20
    p.drawString(100, y_position, f"Total de Marcas: {total_marcas}")
    y_position -= 20
    p.drawString(100, y_position, f"Total de Nutricionistas: {total_nutricionistas}")
    y_position -= 20
    p.drawString(100, y_position, f"Total de Usuarios Sin Asignar: {total_sin_asignar}")
    y_position -= 30


    if y_position - 320 < 0:
        p.showPage()
        y_position = height - 50
    
   
    p.drawImage(pie_chart_file.name, 100, y_position - 320, width=200, height=200)

    p.drawImage(bar_chart_file.name, 320, y_position - 320, width=200, height=200)

    y_position -= 40
    p.drawString(100, y_position, f"Total de Usuarios: {total_usuarios}")

  
    p.save()

    return response

generar_reporte_pdf_tipos.short_description = "Generar reporte PDF de usuarios por tipo"


def generar_reporte_excel_tipos(modeladmin, request, queryset):
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Usuarios"

    
    ws.append(["Usuario", "Tipo"])

    total_deportistas = Deportista.objects.count()
    total_patrocinadores = Patrocinador.objects.count()
    total_marcas = Marca.objects.count()
    total_nutricionistas = Nutricionista.objects.count()
    total_usuarios = queryset.count()
 
    ws.append([])
    ws.append(["Total de Deportistas", total_deportistas])
    ws.append(["Total de Patrocinadores", total_patrocinadores])
    ws.append(["Total de Marcas", total_marcas])
    ws.append(["Total de Nutricionistas", total_nutricionistas])
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


class DeportistaAdmin(admin.ModelAdmin):
    list_display = ('usuario','deporte')


class NutricionistasAdmin(admin.ModelAdmin):
    list_display = ('usuario','especialidad')


class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('usuario','deportistas_interes')

class MarcasAdmin(admin.ModelAdmin):
    list_display = ('usuario','razon_social')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deportista, DeportistaAdmin)
admin.site.register(Nutricionista, NutricionistasAdmin)
admin.site.register(Patrocinador, PatrocinadorAdmin)
admin.site.register(Marca, MarcasAdmin)
admin.site.register(Pqrs)
admin.site.register(Contenido)
admin.site.register(Parametros)

