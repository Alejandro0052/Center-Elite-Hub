from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics

@api_view(['POST'])
def register_user(request):
    data = request.data
    user_type = data.get('user_type')  

    user_serializer = UsuarioSerializer(data=data)
    if user_serializer.is_valid():
        user = user_serializer.save()

       
        if user_type == 'Deportista':
            Group.objects.get(name='Deportista').user_set.add(user)
        elif user_type == 'Patrocinador':
            Group.objects.get(name='Patrocinador').user_set.add(user)
        else:
            return Response({"error": "Tipo de usuario no válido"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



@api_view(['POST'])
def upload_image(request):
    user = request.user
    image = request.FILES.get('image')

    if not image:
        return Response({"error": "No se ha proporcionado ninguna imagen."}, status=status.HTTP_400_BAD_REQUEST)
    
    user.imagen_de_perfil = image
    user.save()
    return Response({"message": "Imagen subida exitosamente."}, status=status.HTTP_200_OK)