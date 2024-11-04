from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Usuario, Deportista, Patrocinador, Marca, Nutricionista, Pqrs, Contenido, Deporte, User, Parametros
from django.contrib.auth import authenticate

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'direccion', 'edad', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            direccion=validated_data.get('direccion', ''),
            edad=validated_data.get('edad', 0)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username','first_name', 'last_name', 'direccion', 'edad','password' , 'imagen_de_perfil']

    def create(self, validated_data):
        user = Usuario(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            direccion=validated_data['direccion'],
            edad=validated_data['edad'],
            username=validated_data['username'],  
            imagen_de_perfil=validated_data.get('imagen_de_perfil'),  

        )
        user.set_password(validated_data['password']) 
        user.save()
        return user

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
        model = Nutricionista
        fields = ['usuario', 'especialidad']

    def create(self, validated_data):
        # Extraemos los datos del usuario
        usuario_data = validated_data.pop('usuario')
        
        # Creamos la instancia de Usuario
        usuario = Usuario.objects.create(**usuario_data)
        
        # Creamos y retornamos la instancia de Nutricionista
        nutricionista = Nutricionista.objects.create(usuario=usuario, **validated_data)
        return nutricionista


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

class ParametrosSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Parametros
        fields = ['contactenos','terminos_condiciones', 'quienes_somos','politica_tratamiento_datos']

