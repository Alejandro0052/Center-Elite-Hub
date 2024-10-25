from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario, Deporte, Deportista, Pqrs, Patrocinador, Contenido, Nutricionista, Marca

class UsuarioCreationForm(forms.ModelForm):
    """
    Un formulario para crear nuevos usuarios. Incluye todos los campos personalizados,
    junto con la contraseña.
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil')  # Incluimos los campos personalizados aquí

    def clean_password2(self):
        # Verifica que ambas contraseñas coincidan
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Encripta la contraseña al guardarla
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UsuarioChangeForm(forms.ModelForm):
    """
    Un formulario para actualizar usuarios. Incluye todos los campos, pero
    reemplaza el campo de contraseña por el campo de contraseña hasheada.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

    def clean_password(self):
        # Devuelve el valor original de la contraseña
        return self.initial["password"]

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),  # Agregamos 'groups' y 'user_permissions'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'numero_telefono', 'direccion', 'edad', 'imagen_de_perfil', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),  # Incluimos los campos personalizados y permisos
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')  # Para permitir la selección de múltiples permisos

# Registro del admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)
admin.site.register(Pqrs)
admin.site.register(Contenido)