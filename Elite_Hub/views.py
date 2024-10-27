from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


def home(request):
    admin_url = reverse('admin:index')
    html = f"""
        <html>
            <head>
                <title>Página de Inicio</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f3f4f6;
                        color: #333;
                        text-align: center;
                        margin: 0;
                        padding: 20px;
                    }}
                    h1 {{
                        color: #2c3e50;
                    }}
                    p {{
                        color: #7f8c8d;
                        font-size: 1.1em;
                    }}
                    .button {{
                        background-color: #3498db;
                        color: white;
                        padding: 12px 24px;
                        text-decoration: none;
                        font-size: 16px;
                        border-radius: 8px;
                        border: none;
                        cursor: pointer;
                    }}
                    .button:hover {{
                        background-color: #2980b9;
                    }}
                </style>
            </head>
            <body>
                <h1>Bienvenido a Elite Hub</h1>
                <p>Haz clic en el siguiente botón para ir al administrador.</p>
                <a href="{admin_url}">
                    <button class="button">Ir al Admin</button>
                </a>
            </body>
        </html>
    """
    return HttpResponse(html)

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
