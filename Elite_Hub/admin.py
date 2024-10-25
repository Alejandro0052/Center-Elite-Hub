from django.contrib import admin
from Elite_Hub.models import Usuario, Deporte, Deportista, Nutricionista, Patrocinador, Marca, Contenido, Pqrs
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

Usuario = get_user_model()

class UsuarioCreationForm(forms.ModelForm):
    """
    Un formulario para crear nuevos usuarios. Incluye los campos de contraseña
    y repite la contraseña.
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name')  # Incluimos 'username' aquí

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
    Un formulario para actualizar usuarios. Incluye todos los campos del usuario,
    pero reemplaza el campo de contraseña por el campo de contraseña hasheada.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'is_active', 'is_staff')  # Incluimos 'username' aquí

    def clean_password(self):
        # Devuelve el valor original de la contraseña
        return self.initial["password"]

# Registro del admin personalizado
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Incluimos 'username' en 'list_display'
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),  # Añadimos 'username' en fieldsets
        ('Información personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}  # Añadimos 'username'
        ),
    )
    search_fields = ('username', 'email')  # Hacemos el campo 'username' searchable
    ordering = ('email',)
    filter_horizontal = ()

# Registra el nuevo UserAdmin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Nutricionista)
admin.site.register(Patrocinador)
admin.site.register(Marca)
admin.site.register(Pqrs)
admin.site.register(Contenido)
