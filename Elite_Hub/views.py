from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Nutricionista, Deportista , Patrocinador, Marca, Pqrs, Contenido, Parametros
from .serializers import NutricionistaSerializer, DeportistaSerializer, PatrocinadorSerializer, MarcasSerializer, PqrsSerializer, ContenidoSerializer
from .serializers import RegisterSerializer, ParametrosSerializer
from django.http import JsonResponse
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny



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


class RegisterUser(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario registrado con exito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class NutricionistaListView(APIView):
    def get(self, request):
        nutricionistas = Nutricionista.objects.all()
        serializer = NutricionistaSerializer(nutricionistas, many=True)
        return Response(serializer.data)

class DeportistaListView(APIView):
    def get(self, request):
        deportistas = Deportista.objects.all()
        serializer = DeportistaSerializer(deportistas, many=True)
        return Response(serializer.data)
    
class PatrocinadorListView(APIView):
    def get(self, request):
        patrocinador = Patrocinador.objects.all()
        serializer = PatrocinadorSerializer(patrocinador, many=True)
        return Response(serializer.data)
    

class MarcaListView(APIView):
    def get(self, request):
        marca = Marca.objects.all()
        serializer = MarcasSerializer(marca, many=True)
        return Response(serializer.data)

class PqrsListView(APIView):
    def get(self, request):
        pqrs = Pqrs.objects.all()
        serializer = PqrsSerializer(pqrs, many=True)
        return Response(serializer.data)
    
class ContenidoListView(APIView):
    def get(self, request):
        contenido = Contenido.objects.all()
        serializer = ContenidoSerializer(contenido, many=True)
        return Response(serializer.data)
    
class ParametrosListView(APIView):
    def get(self, request):
        parametros = Parametros.objects.all()
        serializer = ParametrosSerializer(parametros, many=True)
        return Response(serializer.data)

    