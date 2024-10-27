from rest_framework import serializers
from .models import Usuario, Deportista, Patrocinador, Marca, Nutricionista, Pqrs, Contenido, Deporte

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','correo','direccion', 'edad'] #'imagen_perfil

class DeportistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Deportista
        fields = ['usuario', 'deporte']

class DeporteSerializer(serializers.ModelSerializer):
    deportista = DeportistaSerializer()

    class Meta:
        model = Deporte
        fields = ['deportista','deporte']
class PatrocinadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Patrocinador
        fields = ['usuario']

class NutricionistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model =  Nutricionista
        fields = ['usuario']

class PqrsSerializer(serializers.ModelSerializer):
    Usuario = UsuarioSerializer()

    class Meta:
        model = Pqrs
        fields = ['usuario']

class ContenidoSerializer(serializers.ModelSerializer):
    Usuario = UsuarioSerializer()

    class Meta:
        model = Contenido
        fields = ['usuario']

class MarcasSerializer(serializers.ModelSerializer):
    Usuario = UsuarioSerializer()

    class Meta:
        model = Marca
        fields = ['usuario']

