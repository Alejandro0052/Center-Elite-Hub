from rest_framework import serializers
from .models import Usuario, Deportista, Patrocinador, Marca, Nutricionista, Pqrs, Contenido, Deporte, User, Parametros

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'direccion', 'edad','username','password']  # 'imagen_de_perfil',

    def create(self, validated_data):
        # Crea un nuevo usuario basado en el modelo Usuario
        user = Usuario(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            direccion=validated_data['direccion'],
            edad=validated_data['edad'],
            username=validated_data['username'],  
            #imagen_de_perfil=validated_data.get('imagen_de_perfil'),  

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

class ParametrosSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Parametros
        fields = ['contactenos','terminos_condiciones', 'quienes_somos','politica_tratamiento_datos']

