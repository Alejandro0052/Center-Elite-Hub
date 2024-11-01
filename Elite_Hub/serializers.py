from rest_framework import serializers
from .models import Usuario, Deportista, Patrocinador, Marca, Nutricionista, Pqrs, Contenido, Deporte, User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()
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
        fields = ['usuario','especialidad']

class PqrsSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Pqrs
        fields = ['usuario','tipo','asunto','descripcion','imagen_de_evidencia']

class ContenidoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Contenido
        fields = ['usuario','titulo','descripcion','contenido_imagen']

class MarcasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Marca
        fields = ['usuario','razon_social']

