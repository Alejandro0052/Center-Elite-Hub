from rest_framework import serializers
from .models import Usuario, Deportista, Patrocinador, Marca, Nutricionista, Pqrs, Contenido, Deporte


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email']  # Incluye todos los campos necesarios, como username y password

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name','direccion', 'edad', 'imagen_de_perfil'] #'imagen_perfil


class DeportistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Deportista
        fields = ['usuario', 'deporte','descripcion']


class DeporteSerializer(serializers.ModelSerializer):
    deportista = DeportistaSerializer()

    class Meta:
        model = Deporte
        fields = ['deportista','deporte']

class PatrocinadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Patrocinador
        fields = ['usuario','deportistas_interes'] 

class NutricionistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model =  Nutricionista
        fields = ['usuario', 'especialidad']

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
        fields = ['usuario', 'razon_social']

