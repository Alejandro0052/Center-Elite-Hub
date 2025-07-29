from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Eventos, Usuario, Deportista, Publicacion, Patrocinador, Noticias, Marca, Nutricionista, Pqrs, Contenido, Deporte, User, Parametros, Testimonios
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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials.')
            data['user'] = user
        else:
            raise serializers.ValidationError('Both username and password are required.')
        return data
    
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


class UsuarioPublicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','first_name','last_name','direccion','edad','email']




class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','username','first_name', 'last_name', 'direccion', 'edad','email'] #, 'imagen_de_perfil'

    def create(self, validated_data):
        user = Usuario(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
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
    imagen_de_perfil = serializers.ImageField(use_url=True)

    class Meta:
        model = Deportista
        fields = ['usuario', 'deporte','descripcion', 'imagen_de_perfil']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Genera la URL completa para la imagen
        request = self.context.get('request')
        if instance.imagen_de_perfil and request:
            representation['imagen_de_perfil'] = request.build_absolute_uri(instance.imagen_de_perfil.url)
        return representation


class PatrocinadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    imagen_de_perfil = serializers.ImageField(use_url=True)

    class Meta:
        model = Patrocinador
        fields = ['usuario','imagen_de_perfil','deportistas_interes','descripcion'] 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Genera la URL completa para la imagen
        request = self.context.get('request')
        if instance.imagen_de_perfil and request:
            representation['imagen_de_perfil'] = request.build_absolute_uri(instance.imagen_de_perfil.url)
        return representation
    
    

class NutricionistaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    imagen_de_perfil = serializers.ImageField(use_url=True)

    class Meta:
        model = Nutricionista
        fields = ['usuario', 'especialidad','nivel_estudios','descripcion','imagen_de_perfil']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        usuario = Usuario.objects.create(**usuario_data)
        
       
        nutricionista = Nutricionista.objects.create(usuario=usuario, **validated_data)
        return nutricionista
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.imagen_de_perfil and request:
            representation['imagen_de_perfil'] = request.build_absolute_uri(instance.imagen_de_perfil.url)
        return representation


class NoticiasSerializer(serializers.ModelSerializer):
    foto_noticia = serializers.ImageField(use_url=True)

    class Meta:
        model = Noticias
        fields = ['titulo','texto_noticia','fecha','foto_noticia']


class EventosSerializer(serializers.ModelSerializer):
    evento_imagen = serializers.ImageField(use_url=True)

    class Meta:
        model = Eventos
        fields = ['titulo','descripcion','evento_imagen','fecha']

class TestimoniosSerializer(serializers.ModelSerializer):
    testimonio_imagen = serializers.ImageField(use_url=True)

    class Meta:
        model = Testimonios
        fields = ['titulo','descripcion','testimonio_imagen','fecha']

class PublicacionesSerializer(serializers.Serializer):
    imagen = serializers.ImageField(use_url=True)

    class Meta:
        model = Publicacion
        fields = ['texto','imagen','fecha_creacion']



class PqrsSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField()  
    class Meta:
        model = Pqrs
        fields = ['usuario', 'tipo', 'asunto', 'descripcion']  #,'imagen_de_evidencia'

    def validate_usuario(self, username):
        try:
            usuario = Usuario.objects.get(username=username)
            return usuario
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Error.")
    
    def create(self, validated_data):
        usuario = validated_data.pop('usuario')
        return Pqrs.objects.create(usuario=usuario, **validated_data)



class ContenidoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Contenido
        fields = ['usuario','titulo','descripcion','contenido_imagen']

class MarcasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    imagen_de_perfil = serializers.ImageField(use_url=True)

    class Meta:
        model = Marca
        fields = ['usuario','razon_social','imagen_de_perfil','descripcion','fecha']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Genera la URL completa para la imagen
        request = self.context.get('request')
        if instance.imagen_de_perfil and request:
            representation['imagen_de_perfil'] = request.build_absolute_uri(instance.imagen_de_perfil.url)
        return representation

class ParametrosSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Parametros
        fields = ['contactenos','terminos_condiciones', 'quienes_somos','politica_tratamiento_datos']

class DeporteSerializer(serializers.ModelSerializer):
    deportista = DeportistaSerializer()
    imagen_de_perfil = serializers.ImageField(use_url=True)

    class Meta:
        model = Deporte
        fields = ['deportista','deporte']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        usuario = Usuario.objects.create(**usuario_data)
        
       
        deportista = Deportista.objects.create(usuario=usuario, **validated_data)
        return deportista
    